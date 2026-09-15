# Additional Resources · Week 17
## 145060 Programming · Week 17
### Topic: secure coding, common vulnerabilities, and CIA

Links marked **Confident** or **[VERIFY]**, same standard as every week. Monday introduces
no new concept; its review set comes from the Unit 7 Gate 1 bank and earlier unit banks, so
no outside link is assigned for it.

| # | Resource | For | Level | Time |
|---|---|---|---|---|
| 1 | OWASP Top Ten overview | Tue-Wed | On-level | 25 min |
| 2 | Official docs: why eval is dangerous | Tue | On-level | 10 min |
| 3 | CIA triad explainer | Thu | On-level | 12 min |
| 4 | Path traversal explained | Wed | On-level | 12 min |
| 5 | A current article on a real breach | Thu | Extension | 15 min |
| 6 | The anchor v4 security notes | Tue | Extension | 15 min |
| 7 | SQ-05 Bug Hunt (review) | Fri | Extension | 1 block |

---

## 1. Primary reading

**The OWASP Top Ten overview** · `https://owasp.org/www-project-top-ten/` · **[VERIFY]** the
exact URL before assigning; OWASP reorganizes, but the project is stable and simple to find by
searching "OWASP Top Ten."

**Why this one.** It is the industry's plain-language list of the most common web
vulnerabilities, several of which this week teaches: injection, broken access, security
misconfiguration. Read the category names and one-line descriptions, not the deep detail.

**Skip:** the framework-specific mitigations. Read for the categories and why each matters.

---

## 2. Official documentation, on eval

The Python documentation for `eval`, which describes what it does. ·
`https://docs.python.org/3/library/functions.html#eval` · **Confident.**

**Assign a question, not the page.**

> Read what `eval` does. In one sentence, why is running `eval` on text a user typed
> dangerous?

That settles Tuesday's arbitrary-code-execution lesson from the primary source.

---

## 3. The CIA triad, explained

A reputable plain-language explainer of confidentiality, integrity, and availability. Search
"CIA triad confidentiality integrity availability." · **[VERIFY]** the URL before assigning.

**Why this one.** Thursday is CIA. A short outside explainer, with examples different from
ours, reinforces the three definitions. If you cannot verify one, the `Notes_Confidentiality
IntegrityAvailability` lecture notes cover it fully.

---

## 4. Path traversal, explained

A short, reputable explainer of directory traversal, for example the OWASP page on path
traversal. · **[VERIFY]** the URL before assigning.

**Why this one.** Wednesday's deliberate error is a path traversal. Seeing the `..` attack
described by a security source, with the same shape as our `../../settings.py`, connects the
lab to the real category.

---

## 5. A current article on a real breach

A recent, reputable news article about a breach caused by one of this week's categories: a
leaked key in a public repository, a path traversal, an injection. · **[VERIFY]** and pick
one current the week you teach. Do not name a specific company or incident from memory here,
because details matter and get remembered wrong.

**Why this one.** The categories feel abstract until a student sees one cost a real
organization real money. Choose one that matches a category from the lab.

---

## 6. The anchor project's security design

`Courses/145060/anchor-project/text-adventure/v4/README.md`, the sections on untrusted
input and no credentials. · **Confident**, it is in this repository.

**Why this one.** The text adventure was built with this week's lessons already applied: the
`examine` input is capped and filtered, the model reply is checked and stripped, and a test
fails if a credential appears. Read it as an example of secure coding done on purpose.

---

## 7. Side quest

**SQ-05 Bug Hunt**, revisited as review. Finding planted defects in code you did not write is
the same muscle as the security review lab. Full description in
`Courses/Misc/side-quests/SQ-05-Bug-Hunt/`. · **Confident**, it is in this repository.

**Why it fits here.** SQ-05's lesson, that a passing test suite is not proof of safety, is
exactly Friday's Gate 2 and the bonus defect in the security lab.

---

## For the student who is behind

1. The `Notes_VulnerabilitiesAndSecureCoding` lecture notes, one category at a time
2. Run the vulnerable Study Hall app and reproduce two defects with the recorded commands
3. The CIA one-liners, then sort five scenarios into C, I, and A

Do not assign all seven. A student who is behind and gets seven links reads none.
