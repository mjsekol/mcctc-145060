"""Acceptance tests for Lab U7-01 Gear Locker.

Run one part at a time from the folder that holds gear_locker.py:

    python -m unittest -v test_gear_locker.Part1Tests
    python -m unittest -v test_gear_locker.Part2Tests
    python -m unittest -v test_gear_locker.Part3Tests

Run everything:

    python -m unittest -v test_gear_locker

A failing test tells you WHAT is wrong, not WHERE. You may read this file.
You may not edit it. Changing a test until it passes hides a bug.
"""

import unittest

import gear_locker
from gear_locker import Gear


class Part1Tests(unittest.TestCase):
    """Tuesday: __init__ and attributes."""

    def test_a_new_gear_remembers_what_it_was_given(self):
        pad = Gear("CTRL-01", "controller", "worn")
        self.assertEqual(pad.tag, "CTRL-01")
        self.assertEqual(pad.kind, "controller")
        self.assertEqual(pad.condition, "worn")

    def test_condition_defaults_to_good(self):
        self.assertEqual(Gear("HEAD-01", "headset").condition, "good")

    def test_new_gear_starts_in_the_cabinet(self):
        pad = Gear("CTRL-01", "controller")
        self.assertIsNone(pad.borrower)
        self.assertEqual(pad.times_loaned, 0)

    def test_two_objects_do_not_share_attributes(self):
        first = Gear("CTRL-01", "controller")
        second = Gear("CTRL-02", "controller")
        first.condition = "broken"
        self.assertEqual(second.condition, "good")

    def test_an_unknown_condition_is_refused(self):
        with self.assertRaises(ValueError):
            Gear("CTRL-01", "controller", "sticky")


class Part2Tests(unittest.TestCase):
    """Wednesday: methods and self."""

    def setUp(self):
        self.pad = Gear("CTRL-01", "controller")

    def test_is_available_returns_a_real_true_or_false(self):
        self.assertIs(self.pad.is_available(), True)
        self.pad.check_out("NovaFox")
        self.assertIs(self.pad.is_available(), False)

    def test_check_out_records_the_borrower_and_counts_the_loan(self):
        message = self.pad.check_out("NovaFox")
        self.assertEqual(self.pad.borrower, "NovaFox")
        self.assertEqual(self.pad.times_loaned, 1)
        self.assertIn("NovaFox", message)

    def test_gear_already_out_is_not_lent_twice(self):
        self.pad.check_out("NovaFox")
        message = self.pad.check_out("PixelMoth")
        self.assertEqual(self.pad.borrower, "NovaFox")
        self.assertEqual(self.pad.times_loaned, 1)
        self.assertIn("already out", message)

    def test_broken_gear_is_never_available(self):
        broken = Gear("CTRL-03", "controller", "broken")
        self.assertIs(broken.is_available(), False)
        broken.check_out("NovaFox")
        self.assertIsNone(broken.borrower)

    def test_check_in_clears_the_borrower_and_records_condition(self):
        self.pad.check_out("NovaFox")
        self.pad.check_in("worn")
        self.assertIsNone(self.pad.borrower)
        self.assertEqual(self.pad.condition, "worn")

    def test_label_is_one_line_with_the_tag(self):
        label = self.pad.label()
        self.assertIn("CTRL-01", label)
        self.assertNotIn("\n", label)


class Part3Tests(unittest.TestCase):
    """Thursday: objects working together."""

    def setUp(self):
        self.locker = gear_locker.build_locker()

    def test_find_matches_tags_in_any_case(self):
        self.assertIs(self.locker.find("ctrl-01"), self.locker.find("CTRL-01"))
        self.assertIsNotNone(self.locker.find(" ctrl-01 "))

    def test_unknown_tag_gives_a_message_not_a_crash(self):
        message = self.locker.check_out("CTRL-99", "NovaFox")
        self.assertIn("CTRL-99", message)

    def test_locker_check_out_changes_the_gear_object_itself(self):
        self.locker.check_out("CTRL-01", "NovaFox")
        self.assertEqual(self.locker.find("CTRL-01").borrower, "NovaFox")

    def test_available_skips_borrowed_and_broken_gear(self):
        self.locker.check_out("CTRL-01", "NovaFox")
        tags = [gear.tag for gear in self.locker.available()]
        self.assertEqual(tags, ["CTRL-02", "HEAD-01"])

    def test_two_lockers_do_not_share_gear(self):
        other = gear_locker.GearLocker("Robotics Club")
        self.assertEqual(len(other.items), 0)
        self.assertEqual(len(self.locker.items), 4)

    def test_report_ends_with_the_ready_count(self):
        self.locker.check_out("HEAD-01", "PixelMoth")
        self.assertTrue(self.locker.report().endswith("2 of 4 ready to lend"))


if __name__ == "__main__":
    unittest.main()
