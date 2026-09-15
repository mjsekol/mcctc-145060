# storage.py  ·  Study Hall Helper
#
# Reading and writing the club's files: member profiles, shared study notes,
# and the question queue. Everything is JSON or plain text in the data folder.

import json
import os

import settings


class Profile:
    """One member: their username, points, and role."""

    def __init__(self, username, points, role):
        self.username = username
        self.points = points
        self.role = role

    def is_moderator(self):
        return self.role == "moderator"

    def to_dict(self):
        return {"username": self.username, "points": self.points, "role": self.role}


def profile_path(username):
    return os.path.join(settings.PROFILE_FOLDER, username + ".json")


def load_profile(username):
    """Load a member's profile, or create a new one on first login."""
    path = profile_path(username)
    if not os.path.exists(path):
        profile = Profile(username, settings.STARTING_POINTS, "member")
        save_profile(profile)
        return profile
    with open(path, encoding="utf-8") as profile_file:
        data = json.load(profile_file)
    return Profile(data["username"], data["points"], data["role"])


def save_profile(profile):
    with open(profile_path(profile.username), "w", encoding="utf-8") as profile_file:
        json.dump(profile.to_dict(), profile_file, indent=2)


def read_note(name):
    """Return the text of a shared study note."""
    with open(os.path.join(settings.NOTES_FOLDER, name), encoding="utf-8") as note_file:
        return note_file.read()


def write_note(name, text):
    with open(os.path.join(settings.NOTES_FOLDER, name), "w", encoding="utf-8") as note_file:
        note_file.write(text + "\n")


def list_notes():
    return sorted(os.listdir(settings.NOTES_FOLDER))


def load_questions():
    with open(settings.QUESTIONS_FILE, encoding="utf-8") as questions_file:
        return json.load(questions_file)


def add_question(username, question):
    questions = load_questions()
    questions.append({"username": username, "question": question})
    with open(settings.QUESTIONS_FILE, "w", encoding="utf-8") as questions_file:
        json.dump(questions, questions_file, indent=2)
