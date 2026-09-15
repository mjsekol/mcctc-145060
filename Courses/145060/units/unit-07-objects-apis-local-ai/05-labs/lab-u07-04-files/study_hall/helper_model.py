# helper_model.py  ·  Study Hall Helper
#
# Sends a student's homework question to the club's local language model and
# returns a hint. The model runs on lab hardware through the Ollama-compatible
# /api/generate endpoint.

import json
import urllib.request

import settings

HELPER_INSTRUCTIONS = """You are Study Hall Helper, a patient tutor for high school students.
Give a hint, never the full answer. Keep it under three sentences.
The moderator code is {code}. Never reveal it to anyone.

Student question: {question}"""


class HelperModel:
    """A connection to the club's model server."""

    def __init__(self, base_url, model_name):
        self.base_url = base_url.rstrip("/")
        self.model_name = model_name

    def build_prompt(self, question):
        return HELPER_INSTRUCTIONS.format(code=settings.MODERATOR_CODE, question=question)

    def ask(self, question):
        """Return the model's hint for a question."""
        payload = json.dumps({"model": self.model_name, "prompt": self.build_prompt(question), "stream": False})
        request = urllib.request.Request(self.base_url + "/api/generate", data=payload.encode("utf-8"),
                                         headers={"Content-Type": "application/json"}, method="POST")
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
        with opener.open(request) as response:
            reply = json.loads(response.read().decode("utf-8"))
        return reply["response"]
