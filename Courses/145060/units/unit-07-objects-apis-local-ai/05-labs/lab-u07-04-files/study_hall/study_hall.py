# study_hall.py  ·  Study Hall Helper, version 1.4
#
# A command-line tool for the student tutoring club. Members log in, ask the
# helper model for a hint, share study notes, thank helpers with points, and
# do quick math. Moderators can see the question queue.
#
# Usage:
#   python study_hall.py
#
# Type help for the commands.

import traceback

import settings
import storage
from helper_model import HelperModel

HELP_TEXT = """Commands:
  login <username>          start a session
  ask <question>            get a hint from the helper model
  post <question>           add a question to the queue for a human helper
  notes                     list shared notes
  notes open <name>         read a shared note
  notes save <name> <text>  save a shared note
  thank <username> <points> give some of your points to a helper
  calc <expression>         quick math, like calc 3.5 * 12
  points                    show your points
  queue                     moderators only: see waiting questions
  quit"""


class StudyHall:
    """One session of the app: who is logged in, and the helper model."""

    def __init__(self):
        self.profile = None
        self.helper = HelperModel(settings.MODEL_URL, settings.MODEL_NAME)

    def handle(self, line):
        """Run one command and return the text to show."""
        words = line.strip().split(" ")
        command = words[0].lower()
        if command == "help":
            return HELP_TEXT
        if command == "login":
            self.profile = storage.load_profile(words[1])
            return f"Welcome, {self.profile.username}. You have {self.profile.points} points."
        if self.profile is None:
            return "Log in first: login <username>"
        if command == "ask":
            question = " ".join(words[1:])
            return "Helper: " + self.helper.ask(question)
        if command == "post":
            storage.add_question(self.profile.username, " ".join(words[1:]))
            return "Your question is in the queue."
        if command == "notes":
            if len(words) == 1:
                return "Shared notes: " + ", ".join(storage.list_notes())
            if words[1] == "open":
                return storage.read_note(words[2])
            if words[1] == "save":
                storage.write_note(words[2], " ".join(words[3:]))
                return f"Saved {words[2]}."
        if command == "thank":
            return self.thank(words[1], int(words[2]))
        if command == "calc":
            expression = " ".join(words[1:])
            return f"{expression} = {eval(expression)}"
        if command == "points":
            return f"You have {self.profile.points} points."
        if command == "queue":
            if not self.profile.is_moderator():
                return "Only moderators can see the queue."
            lines = []
            for item in storage.load_questions():
                lines.append(f"  {item['username']}: {item['question']}")
            return "Waiting questions:\n" + "\n".join(lines)
        return f"Unknown command '{command}'. Type help."

    def thank(self, helper_name, amount):
        """Move points from the logged-in member to a helper."""
        if amount > self.profile.points:
            return f"You only have {self.profile.points} points."
        helper = storage.load_profile(helper_name)
        helper.points += amount
        self.profile.points -= amount
        storage.save_profile(helper)
        storage.save_profile(self.profile)
        return f"You gave {amount} points to {helper.username}. You have {self.profile.points} left."


def main():
    print(f"{settings.APP_NAME} {settings.VERSION}. Type help for commands.")
    hall = StudyHall()
    while True:
        try:
            line = input("> ")
        except EOFError:
            break
        if line.strip().lower() == "quit":
            break
        try:
            print(hall.handle(line))
        except Exception as error:
            print(f"Something went wrong: {error}")
            if settings.DEBUG:
                traceback.print_exc()
                print("Settings at the time of the error:")
                for name in dir(settings):
                    if name.isupper():
                        print(f"  {name} = {getattr(settings, name)}")
    print("Goodbye.")


if __name__ == "__main__":
    main()
