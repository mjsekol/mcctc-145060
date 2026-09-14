# check_ready.py
# Checks whether playlist_namer.py is ready to deploy, the way Render will run it.
#
# Run it from the folder that holds playlist_namer.py:
#   python check_ready.py
#
# It starts your app as a separate program with PORT set to a port it picked,
# points the model at an address where nothing is listening, makes real web
# requests, and stops your app when it is done. It never changes your files.
#
# PASS means the check worked. FAIL says what it saw. SKIP means this machine
# cannot run that check, which is not your fault and not a pass.

import os
import socket
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
APP = HERE / "playlist_namer.py"
STARTUP_SECONDS = 10
PAGE_SECONDS = 15

# Talk to this machine directly. A school proxy must not get in the way.
DIRECT = urllib.request.build_opener(urllib.request.ProxyHandler({}))


def free_port():
    with socket.socket() as probe:
        probe.bind(("127.0.0.1", 0))
        return probe.getsockname()[1]


def network_address():
    """This machine's address on its network, or None if it only has 127.0.0.1."""
    try:
        address = socket.gethostbyname(socket.gethostname())
    except OSError:
        return None
    if address.startswith("127."):
        return None
    return address


def start_app(port_text):
    """Start the app. Its output goes to a temporary file, not a pipe.

    A pipe holds only a few thousand characters. An app that prints a long
    traceback into a full pipe stops dead until someone reads it, which would
    look like your app froze when it did not.
    """
    environment = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONDONTWRITEBYTECODE="1")
    environment["PORT"] = port_text
    # Nothing listens on this port, so the model is missing, the way it is on Render.
    environment["PLAYLIST_MODEL_URL"] = f"http://127.0.0.1:{free_port()}"
    output = tempfile.TemporaryFile(mode="w+", encoding="utf-8")
    process = subprocess.Popen([sys.executable, str(APP)], cwd=HERE, env=environment,
                               stdout=output, stderr=subprocess.STDOUT, text=True, encoding="utf-8")
    process.output_file = output
    return process


def get(url, seconds):
    """Return (status, text) for a GET request, or (None, reason) if nothing answered."""
    try:
        with DIRECT.open(url, timeout=seconds) as response:
            return response.status, response.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as error:
        with error:
            return error.code, error.read().decode("utf-8", "replace")
    except (urllib.error.URLError, OSError) as error:
        return None, str(getattr(error, "reason", error))


def wait_until_listening(port):
    deadline = time.monotonic() + STARTUP_SECONDS
    while time.monotonic() < deadline:
        status, _ = get(f"http://127.0.0.1:{port}/", 1)
        if status is not None:
            return True
        time.sleep(0.25)
    return False


def stop(process):
    """Stop the app if it is still running and return everything it printed."""
    if process.poll() is None:
        process.terminate()
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait()
    process.output_file.seek(0)
    text = process.output_file.read()
    process.output_file.close()
    return text


def main():
    if not APP.exists():
        print(f"Cannot find {APP.name}. Put check_ready.py in the same folder as your app.")
        return 1

    results = []

    def record(outcome, name, detail=""):
        results.append(outcome)
        line = f"{outcome:5} {name}"
        if detail:
            line += f"\n      {detail}"
        print(line)

    port = free_port()
    print(f"Starting {APP.name} with PORT={port} and no model...\n")
    process = start_app(str(port))
    try:
        listening = wait_until_listening(port)
        if listening:
            record("PASS", "1. listens on the port in the PORT variable")
        else:
            record("FAIL", "1. listens on the port in the PORT variable",
                   f"nothing answered on port {port} within {STARTUP_SECONDS} seconds")

        address = network_address()
        if not listening:
            record("SKIP", "2. accepts connections from other machines", "check 1 has to pass first")
        elif address is None:
            record("SKIP", "2. accepts connections from other machines", "this machine has no network address to test with")
        else:
            status, detail = get(f"http://{address}:{port}/", 5)
            if status is None:
                record("FAIL", "2. accepts connections from other machines",
                       f"http://{address}:{port}/ was refused ({detail})")
            else:
                record("PASS", "2. accepts connections from other machines")

        if listening:
            start = time.monotonic()
            status, text = get(f"http://127.0.0.1:{port}/health", 5)
            seconds = time.monotonic() - start
            if status == 200 and seconds < 2:
                record("PASS", "3. /health answers 200 in under 2 seconds")
            else:
                record("FAIL", "3. /health answers 200 in under 2 seconds",
                       f"got status {status} after {seconds:.1f} seconds")

            status, text = get(f"http://127.0.0.1:{port}/", 5)
            if status == 200:
                record("PASS", "4. the home page loads")
            else:
                record("FAIL", "4. the home page loads", f"got status {status}")

            status, text = get(f"http://127.0.0.1:{port}/name?mood=rainy+day", PAGE_SECONDS)
            if status == 200 and "saved name" in text.lower():
                record("PASS", "5. a name page still works with no model, labelled as a saved name")
            elif status is None:
                record("FAIL", "5. a name page still works with no model, labelled as a saved name",
                       f"no page came back ({text})")
            else:
                record("FAIL", "5. a name page still works with no model, labelled as a saved name",
                       f"got status {status}; the words 'saved name' {'were' if 'saved name' in text.lower() else 'were not'} on the page")

            status, text = get(f"http://127.0.0.1:{port}/name?mood=%3Cscript%3E", 5)
            if status == 400:
                record("PASS", "6. a mood with symbols in it is refused with 400")
            else:
                record("FAIL", "6. a mood with symbols in it is refused with 400", f"got status {status}")
        else:
            for name in ["3. /health answers 200 in under 2 seconds", "4. the home page loads",
                         "5. a name page still works with no model, labelled as a saved name",
                         "6. a mood with symbols in it is refused with 400"]:
                record("SKIP", name, "check 1 has to pass first")
    finally:
        stop(process)

    process = start_app("not-a-port")
    try:
        process.wait(timeout=STARTUP_SECONDS)
        exited = True
    except subprocess.TimeoutExpired:
        exited = False
    printed = stop(process)
    said_port = "PORT" in printed
    # A traceback names PORT too, because it prints the line that crashed.
    # That is a crash, not a message, so it does not count.
    crashed = "Traceback" in printed
    if exited and process.returncode != 0 and said_port and not crashed:
        record("PASS", "7. PORT=not-a-port stops the app with a message that names PORT")
    elif not exited:
        record("FAIL", "7. PORT=not-a-port stops the app with a message that names PORT",
               "the app kept running, so it is not reading PORT at all")
    elif crashed:
        record("FAIL", "7. PORT=not-a-port stops the app with a message that names PORT",
               "the app crashed with a traceback instead of printing a message")
    else:
        record("FAIL", "7. PORT=not-a-port stops the app with a message that names PORT",
               f"exit code {process.returncode}; the message {'named' if said_port else 'did not name'} PORT")

    requirements = HERE / "requirements.txt"
    if requirements.exists():
        record("PASS", "8. requirements.txt exists")
    else:
        record("FAIL", "8. requirements.txt exists", "It tells anyone deploying the app what to install. Add one, even if it only has a comment.")

    readme = HERE / "README.md"
    if readme.exists() and "python playlist_namer.py" in readme.read_text(encoding="utf-8", errors="replace"):
        record("PASS", "9. README.md names the start command")
    else:
        record("FAIL", "9. README.md names the start command", "README.md must contain: python playlist_namer.py")

    passed = results.count("PASS")
    print(f"\n{passed} passed, {results.count('FAIL')} failed, {results.count('SKIP')} skipped")
    if results.count("FAIL") == 0 and results.count("SKIP") == 0:
        print("Ready to deploy.")
    return 0 if results.count("FAIL") == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
