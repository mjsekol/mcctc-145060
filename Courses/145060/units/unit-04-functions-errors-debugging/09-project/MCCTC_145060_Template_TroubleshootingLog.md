# Troubleshooting Log Template
## 145060 Programming · Unit 4 · The Six-Step Troubleshooting Method

**What this is for.** The syllabus asks you to select and apply a troubleshooting methodology, then document the problem
and the verified solution. This course uses the **Six-Step Troubleshooting Method**, taught on Monday of Week 9. The notes
are [`MCCTC_145060_Notes_TroubleshootingMethod.md`](../03-lecture-notes/MCCTC_145060_Notes_TroubleshootingMethod.md), and
worked example 3 in them is a complete entry you can model yours on.

**How to use it.** Copy everything from `# Troubleshooting Log` down into a file called `troubleshooting-log.md` in the root of
your text adventure repository. Add one entry each time a bug takes you more than a few minutes, or does not crash, or is one a
classmate is likely to hit too. Write the entry **while** you debug, not afterward. An entry reconstructed from memory loses the
wrong theories, and the wrong theories are the most useful part.

**The rules that make an entry count:**

1. **Reproduction.** Somebody else must be able to make the bug happen from what you wrote: the command, the exact input, the
   expected result, and the actual result.
2. **Theory.** At least one specific theory that could have turned out false. "Something is wrong" does not count.
3. **Test.** For every theory, the experiment you ran and its **real** output, pasted, not remembered.
4. **Fix.** The line or lines before and after. One change per attempt.
5. **Verification.** The reproduction run again **and** at least one case that already worked, with real output.

A theory that turned out wrong stays in the entry. Mark it WRONG and write what the test showed.

**For text adventure v2:** at least **two** entries from real bugs you hit while building v2, dated during the build, and **at least one**
of them a bug that did not crash.

**Keep personal information out.** No real names other than your own, no passwords, no school logins, and nothing about anybody else,
in any entry or in any output you paste.

---
---

# Troubleshooting Log

**Project:** ______________________ **Author:** ______________________

**Method:** Six-Step Troubleshooting Method: 1 Identify the problem · 2 Establish a theory · 3 Test the theory · 4 Plan and implement
the fix · 5 Verify · 6 Document

---

## Entry 1 · `file_name.py` · Day, Month Date

### 1. Identify the problem

| | |
|---|---|
| **Command I ran** | |
| **Exact input** | |
| **Expected** | |
| **Actual** | |
| **Crash or silent?** | |

Error message or wrong output, pasted exactly:

```
paste it here
```

### 2 and 3. Theories and tests

Repeat this block for every theory, in the order you tried them.

**Theory 1:** 

**Test of theory 1:** what I ran

```
paste the real output here
```

**Result:** RIGHT or WRONG, and what the output showed:

### 4. Plan and implement the fix

**Why this fixes the cause, in one sentence:**

Before:

```python
paste the old line or lines
```

After:

```python
paste the new line or lines
```

**What else this change could affect:**

### 5. Verify

**The reproduction, run again:**

```
paste the real output here
```

**Cases that already worked, run again:**

```
paste the real output here
```

### 6. What I learned

One or two sentences. What would have found this bug faster, or what will stop it happening again? If this bug should become a test
case, write the test case here.

---

## Entry 2 · `file_name.py` · Day, Month Date

Copy the Entry 1 block again for each new entry.
