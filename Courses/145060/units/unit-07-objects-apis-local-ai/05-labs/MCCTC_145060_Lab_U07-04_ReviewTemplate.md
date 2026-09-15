# Security Review Template
## Study Hall Helper · Reviewer: ______________________

Fill this in as you work. One row per defect. You need at least eight rows, at least one
in each category. Copy this file into your repository and edit it there.

---

## Defect log

For each defect: where it is, how you triggered it, which CIA letter it breaks, and the
fix. The reproduction must be a command someone else could run to see it.

| # | File and line | Category | What goes wrong | Reproduction command | CIA | Fix |
|---|---|---|---|---|---|---|
| 1 |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |
| 3 |  |  |  |  |  |  |
| 4 |  |  |  |  |  |  |
| 5 |  |  |  |  |  |  |
| 6 |  |  |  |  |  |  |
| 7 |  |  |  |  |  |  |
| 8 |  |  |  |  |  |  |
| 9 (bonus) |  |  |  |  |  |  |

**Categories to cover:** input validation, path traversal, secrets in code, unsafe
evaluation, prompt injection, verbose error leakage, missing timeout, save-file integrity.

**CIA:** C for confidentiality (who can read it), I for integrity (whether it is true),
A for availability (whether it is there when you need it). Some defects break more than
one; name the main one and note the others.

---

## Fixes applied

List the defects you fixed. For each, paste the before line and the after line, and the
command that proves the fix holds.

**Fixed defect #___**

- Before:
- After:
- Proof it holds:

**Fixed defect #___**

- Before:
- After:
- Proof it holds:

(Repeat for at least four fixes.)

---

## Five-Dimension Code Review

Score the codebase as a whole on the program's standard rubric. One sentence of evidence
per dimension, drawn from your defect log.

**Correctness (20):** ______ / 20

**Security (20):** ______ / 20

**Readability (20):** ______ / 20

**Performance (20):** ______ / 20

**Requirements Fit (20):** ______ / 20

---

## Summary

Two or three sentences. What is the single most dangerous defect and why. What would you
tell the club before this runs on a shared machine.
