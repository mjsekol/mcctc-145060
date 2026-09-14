# review_check.py
#
# A small static analysis checker built on Python's own ast module.
#
# Static analysis means reading a program WITHOUT running it. This tool turns
# the file into a tree of pieces (a function, a loop, an assignment) and looks
# for patterns a reviewer should stop and examine. It does not decide whether
# the program is correct, and it cannot tell whether the program does what the
# stakeholder asked. A person still has to do that part.
#
# Usage:
#     python review_check.py some_program.py

import ast
import sys

# Names that suggest a value should never be typed into source code.
SECRET_WORDS = ["password", "passwd", "secret", "token", "api_key", "pin"]


def check_secrets(tree, findings):
    """A text value assigned to a secret-looking name is a hardcoded secret (Security)."""
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            is_text = isinstance(node.value, ast.Constant) and isinstance(node.value.value, str)
            for target in node.targets:
                if isinstance(target, ast.Name) and is_text:
                    lowered = target.id.lower()
                    for word in SECRET_WORDS:
                        if word in lowered:
                            findings.append((node.lineno, "Security",
                                             f"'{target.id}' looks like a secret written into the code"))
                            break


def check_eval(tree, findings):
    """eval() and exec() run text as code, so typed input becomes a program (Security)."""
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id in ["eval", "exec"]:
                findings.append((node.lineno, "Security",
                                 f"{node.func.id}() runs text as code"))


def check_swallowed_errors(tree, findings):
    """A bare except, or an except that only says pass, hides failures (Correctness)."""
    for node in ast.walk(tree):
        if isinstance(node, ast.ExceptHandler):
            if node.type is None:
                findings.append((node.lineno, "Correctness",
                                 "bare except catches every error, including your own typos"))
            if len(node.body) == 1 and isinstance(node.body[0], ast.Pass):
                findings.append((node.lineno, "Correctness",
                                 "except block only says pass, so the failure disappears silently"))


def check_docstrings(tree, findings):
    """A function with no docstring makes the next reader guess its purpose (Readability)."""
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if ast.get_docstring(node) is None:
                findings.append((node.lineno, "Readability",
                                 f"function '{node.name}' has no docstring"))


def check_short_names(tree, findings):
    """One-letter names for values and parameters hide meaning (Readability)."""
    reported = set()
    for node in ast.walk(tree):
        names = []
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    names.append((target.id, node.lineno))
        if isinstance(node, ast.FunctionDef):
            for argument in node.args.args:
                names.append((argument.arg, node.lineno))
        for name, line in names:
            if len(name) == 1 and name != "_" and (name, line) not in reported:
                reported.add((name, line))
                findings.append((line, "Readability", f"one-letter name '{name}'"))


def check_open_in_loops(tree, findings):
    """Opening a file inside a loop repeats work on every pass (Performance)."""
    reported = set()
    for loop in ast.walk(tree):
        if isinstance(loop, (ast.For, ast.While)):
            for node in ast.walk(loop):
                is_open = isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "open"
                if is_open and node.lineno not in reported:
                    reported.add(node.lineno)
                    findings.append((node.lineno, "Performance",
                                     "open() inside a loop reads or writes the file on every pass"))


def main():
    """Parse the file named on the command line and print every finding."""
    if len(sys.argv) != 2:
        print("Usage: python review_check.py some_program.py")
        sys.exit(2)

    path = sys.argv[1]
    try:
        with open(path, encoding="utf-8") as file:
            source = file.read()
    except FileNotFoundError:
        print(f"Cannot open {path}")
        sys.exit(2)

    # ast.parse reads the file the same way Python does before running it.
    # A syntax error stops everything here, before any other check can run.
    try:
        tree = ast.parse(source, filename=path)
    except SyntaxError as error:
        print(f"{path}, line {error.lineno}: SyntaxError: {error.msg}")
        sys.exit(1)

    findings = []
    check_secrets(tree, findings)
    check_eval(tree, findings)
    check_swallowed_errors(tree, findings)
    check_docstrings(tree, findings)
    check_short_names(tree, findings)
    check_open_in_loops(tree, findings)
    findings.sort()

    print(f"Static review of {path}")
    print("-" * 60)
    for line, dimension, message in findings:
        print(f"line {line:<4} {dimension:<12} {message}")
    print("-" * 60)
    print(f"{len(findings)} finding(s)")
    print("Not checked by this tool: Requirements Fit, and whether the logic is right.")


if __name__ == "__main__":
    main()
