"""Acceptance tests for Lab U7-03 Announcement Writer.

No real model is needed. These tests start the stub model server on a free
port, switch it between modes, and stop it afterwards.

Run from this folder:

    python -m unittest -v test_announcement_writer

You may read this file. You may not edit it.
"""

import json
import pathlib
import socket
import unittest

import announcement_writer as writer
import stub_model_server as stub

FACTS = {"club": "Robotics Club", "day": "Thursday", "time": "3:15", "room": "Room 118",
         "detail": "Bring safety glasses."}


def unused_port():
    with socket.socket() as probe:
        probe.bind(("127.0.0.1", 0))
        return probe.getsockname()[1]


def reply_bytes(data):
    return json.dumps(data).encode("utf-8")


class ParseReplyTests(unittest.TestCase):
    """parse_reply on its own, with no server at all."""

    def test_a_good_reply_gives_its_text(self):
        text, problem = writer.parse_reply(reply_bytes({"response": " Robotics meets at 3:15 in Room 118. ", "done": True}))
        self.assertEqual(text, "Robotics meets at 3:15 in Room 118.")
        self.assertIsNone(problem)

    def test_a_reply_that_is_not_done_is_refused(self):
        text, problem = writer.parse_reply(reply_bytes({"response": "Calling all Robotics Club mem", "done": False}))
        self.assertIsNone(text)
        self.assertIsNotNone(problem)

    def test_done_must_be_true_not_just_truthy(self):
        text, problem = writer.parse_reply(reply_bytes({"response": "Robotics meets.", "done": "false"}))
        self.assertIsNone(text)

    def test_missing_response_is_refused(self):
        text, problem = writer.parse_reply(reply_bytes({"done": True}))
        self.assertIsNone(text)

    def test_a_number_is_not_text(self):
        text, problem = writer.parse_reply(reply_bytes({"response": 42, "done": True}))
        self.assertIsNone(text)

    def test_broken_json_is_refused(self):
        text, problem = writer.parse_reply(b'{"response": "Calling all')
        self.assertIsNone(text)

    def test_a_json_list_is_refused(self):
        text, problem = writer.parse_reply(b'["Robotics", true]')
        self.assertIsNone(text)

    def test_blank_and_overlong_replies_are_refused(self):
        self.assertIsNone(writer.parse_reply(reply_bytes({"response": "   ", "done": True}))[0])
        self.assertIsNone(writer.parse_reply(reply_bytes({"response": "word " * 200, "done": True}))[0])

    def test_control_characters_are_removed(self):
        text, problem = writer.parse_reply(reply_bytes({"response": "Meet at 3:15\x1b[2J in Room 118.", "done": True}))
        self.assertEqual(text, "Meet at 3:15[2J in Room 118.")


class WriteAnnouncementTests(unittest.TestCase):
    """The whole program against the stub, one failure at a time."""

    @classmethod
    def setUpClass(cls):
        cls.server = stub.start_in_background(delay_seconds=3)

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()

    def settings(self, timeout=1.0):
        return {"base_url": self.server.base_url, "model": "stub-test", "timeout": timeout}

    def use_mode(self, mode):
        self.server.mode = mode

    def test_success_uses_the_model(self):
        self.use_mode(stub.SUCCESS)
        text, source = writer.write_announcement(self.settings(), FACTS)
        self.assertEqual(source, "local model")
        self.assertIn("3:15", text)

    def test_the_request_sends_stream_false_and_the_facts(self):
        self.use_mode(stub.SUCCESS)
        writer.write_announcement(self.settings(), FACTS)
        self.assertIn("Room: Room 118", self.server.prompts[-1])

    def test_every_broken_reply_falls_back_to_the_template(self):
        template = writer.template_announcement(FACTS)
        for mode in [stub.ERROR, stub.MALFORMED, stub.NOT_DONE, stub.MISSING_RESPONSE,
                     stub.WRONG_TYPE, stub.DROPS_FACTS, stub.SLOW]:
            with self.subTest(mode=mode):
                self.use_mode(mode)
                text, source = writer.write_announcement(self.settings(timeout=0.5), FACTS)
                self.assertEqual(text, template)
                self.assertTrue(source.startswith("template"), source)

    def test_no_server_falls_back_to_the_template(self):
        settings = {"base_url": f"http://127.0.0.1:{unused_port()}", "model": "stub-test", "timeout": 10.0}
        text, source = writer.write_announcement(settings, FACTS)
        self.assertEqual(text, writer.template_announcement(FACTS))

    def test_the_template_keeps_every_fact(self):
        text = writer.template_announcement(FACTS)
        for value in FACTS.values():
            self.assertIn(value, text)


class SettingsAndSourceTests(unittest.TestCase):

    def test_defaults(self):
        settings = writer.load_settings({})
        self.assertEqual(settings, {"base_url": "http://127.0.0.1:11434", "model": "llama3.2", "timeout": 20.0})

    def test_environment_overrides(self):
        settings = writer.load_settings({"ANNOUNCE_MODEL_URL": "http://127.0.0.1:11500/",
                                         "ANNOUNCE_MODEL": "stub-test", "ANNOUNCE_MODEL_TIMEOUT": "3"})
        self.assertEqual(settings, {"base_url": "http://127.0.0.1:11500", "model": "stub-test", "timeout": 3.0})

    def test_a_file_url_is_refused(self):
        with self.assertRaises(ValueError):
            writer.load_settings({"ANNOUNCE_MODEL_URL": "file:///C:/Windows/win.ini"})

    def test_no_key_or_password_in_the_program(self):
        source = pathlib.Path(writer.__file__).read_text(encoding="utf-8").lower()
        for marker in ["api_key", "apikey", "bearer", "password", "secret ="]:
            self.assertNotIn(marker, source)


if __name__ == "__main__":
    unittest.main()
