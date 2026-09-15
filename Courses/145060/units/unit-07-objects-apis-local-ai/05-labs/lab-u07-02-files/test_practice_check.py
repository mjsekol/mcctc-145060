"""Acceptance tests for Lab U7-02 Practice Check.

These tests start their own copy of the station feed on a free port and stop
it when they finish. You do not need the server running in another terminal.

Run one part at a time from this folder:

    python -m unittest -v test_practice_check.Part1Tests
    python -m unittest -v test_practice_check.Part2Tests
    python -m unittest -v test_practice_check.Part3Tests

Part 2 takes about 5 seconds, because two of its tests wait on purpose.
You may read this file. You may not edit it.
"""

import pathlib
import socket
import time
import unittest

import practice_check
import weather_station_server as feed

TEST_KEY = "NOT-A-REAL-KEY-test"


def unused_port():
    with socket.socket() as probe:
        probe.bind(("127.0.0.1", 0))
        return probe.getsockname()[1]


def settings_for(server, timeout=2.0, key=TEST_KEY):
    return {"base_url": server.base_url, "timeout": timeout, "key": key}


class FeedTestCase(unittest.TestCase):
    """Starts a feed with a generous rate limit, so only the 429 test hits it."""

    @classmethod
    def setUpClass(cls):
        cls.server = feed.start_in_background(key=TEST_KEY, limit=1000)

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()


class Part1Tests(FeedTestCase):
    """Monday: one request, one JSON reply."""

    def test_get_json_returns_the_station_list_as_a_dictionary(self):
        data = practice_check.get_json(settings_for(self.server), "/api/v1/stations")
        self.assertIsInstance(data, dict)
        ids = [station["id"] for station in data["stations"]]
        self.assertIn("north-field", ids)

    def test_get_json_reads_observations(self):
        data = practice_check.get_json(settings_for(self.server), "/api/v1/stations/north-field/observations")
        self.assertEqual(data["name"], "North Practice Field")
        self.assertEqual(len(data["observations"]), 4)

    def test_decide_says_practice_is_on_for_calm_readings(self):
        readings = [{"observed_at": "2027-01-11T15:45:00", "gust_mph": 12}]
        text = " ".join(practice_check.decide("North Practice Field", readings, 0))
        self.assertIn("PRACTICE IS ON", text)

    def test_decide_moves_inside_at_exactly_the_limit(self):
        readings = [{"observed_at": "2027-01-11T15:45:00", "gust_mph": 30}]
        text = " ".join(practice_check.decide("Stadium", readings, 0))
        self.assertIn("MOVES INSIDE", text)


class Part2Tests(FeedTestCase):
    """Tuesday: every failure gets its own message."""

    def test_unknown_station_is_not_found(self):
        data, problem = practice_check.fetch(settings_for(self.server), "/api/v1/stations/north-feild/observations")
        self.assertIsNone(data)
        self.assertTrue(problem.startswith("NOT FOUND"), problem)

    def test_feed_error_is_its_own_message(self):
        broken = feed.start_in_background(mode=feed.ERROR, key=TEST_KEY, limit=1000)
        try:
            data, problem = practice_check.fetch(settings_for(broken), "/api/v1/stations")
        finally:
            broken.shutdown()
            broken.server_close()
        self.assertTrue(problem.startswith("FEED ERROR"), problem)

    def test_a_web_page_is_not_parsed_as_data(self):
        data, problem = practice_check.fetch(settings_for(self.server), "/api/stations")
        self.assertIsNone(data)
        self.assertTrue(problem.startswith("NOT JSON"), problem)

    def test_timeout_is_its_own_message(self):
        slow = feed.start_in_background(mode=feed.SLOW, delay_seconds=3, key=TEST_KEY, limit=1000)
        try:
            started = time.monotonic()
            data, problem = practice_check.fetch(settings_for(slow, timeout=0.5), "/api/v1/stations")
            elapsed = time.monotonic() - started
        finally:
            slow.shutdown()
            slow.server_close()
        self.assertTrue(problem.startswith("TIMED OUT"), problem)
        self.assertLess(elapsed, 2.5)

    def test_no_server_is_unreachable(self):
        settings = {"base_url": f"http://127.0.0.1:{unused_port()}", "timeout": 10.0, "key": TEST_KEY}
        data, problem = practice_check.fetch(settings, "/api/v1/stations")
        self.assertTrue(problem.startswith("UNREACHABLE"), problem)

    def test_rate_limit_waits_the_retry_after_time_and_tries_again(self):
        strict = feed.start_in_background(key=TEST_KEY, limit=2, window_seconds=1.0)
        waits = []

        def recording_sleep(seconds):
            waits.append(seconds)
            time.sleep(seconds)

        try:
            settings = settings_for(strict)
            practice_check.fetch(settings, "/api/v1/stations", recording_sleep)
            practice_check.fetch(settings, "/api/v1/stations", recording_sleep)
            data, problem = practice_check.fetch(settings, "/api/v1/stations", recording_sleep)
        finally:
            strict.shutdown()
            strict.server_close()
        self.assertIsNone(problem)
        self.assertEqual(waits, [1])

    def test_empty_readings_are_not_calm_weather(self):
        text = " ".join(practice_check.decide("Tennis Courts", [], None))
        self.assertIn("NO DECISION", text)
        self.assertNotIn("PRACTICE IS ON", text)


class Part3Tests(FeedTestCase):
    """Wednesday: settings from the environment, and no secret in the file."""

    def test_defaults_when_nothing_is_set(self):
        settings = practice_check.load_settings({})
        self.assertEqual(settings["base_url"], "http://127.0.0.1:8070")
        self.assertEqual(settings["timeout"], 5.0)
        self.assertEqual(settings["key"], "")

    def test_environment_overrides_every_setting(self):
        settings = practice_check.load_settings({
            "PRACTICE_FEED_URL": "http://127.0.0.1:9999/",
            "PRACTICE_FEED_TIMEOUT": "2.5",
            "PRACTICE_FEED_KEY": "NOT-A-REAL-KEY-abc",
        })
        self.assertEqual(settings, {"base_url": "http://127.0.0.1:9999", "timeout": 2.5,
                                    "key": "NOT-A-REAL-KEY-abc"})

    def test_a_timeout_that_is_not_a_number_is_refused(self):
        with self.assertRaises(ValueError):
            practice_check.load_settings({"PRACTICE_FEED_TIMEOUT": "soon"})

    def test_wrong_key_is_refused_with_its_own_message(self):
        data, problem = practice_check.fetch(settings_for(self.server, key="wrong"),
                                             "/api/v1/stations/track/lightning")
        self.assertTrue(problem.startswith("REFUSED"), problem)

    def test_lightning_moves_practice_inside(self):
        text = practice_check.check_station(settings_for(self.server), "track")
        self.assertIn("MOVES INSIDE", text)

    def test_no_key_is_written_in_the_program(self):
        source = pathlib.Path(practice_check.__file__).read_text(encoding="utf-8")
        self.assertNotIn("NOT-A-REAL-KEY", source)


if __name__ == "__main__":
    unittest.main()
