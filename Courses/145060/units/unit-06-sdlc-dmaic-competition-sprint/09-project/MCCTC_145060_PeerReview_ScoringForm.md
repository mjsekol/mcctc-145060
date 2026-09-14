# Peer Code Review Scoring Form
## 145060 Programming · Unit 6 · Five-Dimension Code Review

Copy this form into a file for each review. Protocol:
[`MCCTC_145060_PeerReview_Protocol.md`](MCCTC_145060_PeerReview_Protocol.md).

---

```markdown
# Peer Code Review · Review <1 or 2>

Team reviewed: <team name>          Reviewing team: <team name>
Date: <date>                        Commit or branch reviewed: <hash or branch name>
Author walking through: <name>      Reader: <name>      Recorder: <name>

## 1. Static analysis

### python -m py_compile <program>.py
<paste the output, or "no output, exit 0">

### python review_check.py <program>.py
<paste the full output>

Static findings a person confirmed as real: <numbers from the list above>
Static findings a person judged to be false alarms, and why: <numbers and reasons>

## 2. Acceptance tests

### python test_<program>.py
Passed: <n>     Failed: <n>
Failing check labels: <labels, or "none">

## 3. Findings

| # | Where (function, line) | Dimension | Consequence | Fix | Severity |
|---|---|---|---|---|---|
| 1 | | | | | must fix / should fix / consider |
| 2 | | | | | |

## 4. One thing this code does well
<Specific. Name the function and why it works.>

## 5. Scores, Five-Dimension Code Review

| Dimension | Score (0-20) | Evidence: finding numbers or a short reason |
|---|---|---|
| Correctness | | |
| Security | | |
| Readability | | |
| Performance | | |
| Requirements Fit | | |
| **Total** | **/100** | |

## 6. Review 2 only: change review questions
1. What the change request asked for:
2. Functions changed on the branch:
3. Other behaviors that depend on them, and whether any changed:
4. Checks passing at v1.0: <n>. Checks passing on the branch: <n>. Checks added: <n>.
5. Validation, checks, or messages removed by the change: <list, or "none found">
6. Anything built that the change request did not ask for:

Recommendation: merge / merge after must-fix findings / do not merge

## 7. Author response (written by the reviewed team, after the review)
| Finding # | Accepted, rejected, or deferred | What we did, or why not | Commit |
|---|---|---|---|
```

---

## Scoring guide, for the reviewers

Score what you found evidence for, not a general impression. A score with no evidence
in column three is not a score.

| Score | Meaning, for any dimension |
|---|---|
| **18-20** | No finding above **consider**. You looked hard, and you can say where. |
| **14-17** | One **should fix**, or several **consider** findings. |
| **10-13** | One **must fix**, or several **should fix** findings. |
| **0-9** | More than one **must fix**, or the dimension could not be checked because the code does not run. |

**Security is scored the same way, and a must-fix security finding caps the Security
score at 9.** Unchecked input and exposed secrets are how small programs cause real
damage, and a review that treats them as minor has missed the point of reviewing.

**Requirements Fit needs the requirements.** Ask the authors for `docs/requirements.md`
before the walkthrough starts. A team that cannot produce it scores 0-9 on this row,
because nothing can be checked against nothing.
