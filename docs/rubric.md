# Documentation Evaluation Rubric

## Overview

This rubric is used to evaluate AI-generated documentation in a consistent and repeatable way.
It is applied by a Validation Agent to assess quality across multiple dimensions.

Each criterion is scored from **1 (Poor)** to **5 (Excellent)**.

---

## Scoring Scale

| Score | Meaning   |
| ----: | --------- |
|     1 | Poor      |
|     2 | Fair      |
|     3 | Good      |
|     4 | Very Good |
|     5 | Excellent |

---

## Evaluation Criteria

### 1. Accuracy

Checks whether the content is technically correct.

**What to look for:**

* Commands are correct
* No hallucinated or outdated steps
* Security guidance is safe and appropriate

---

### 2. Completeness

Checks whether the content covers the full workflow.

**What to look for:**

* All required sections are present
* No missing prerequisites or steps
* End-to-end guidance is provided

---

### 3. Readability

Checks how easy the content is to understand for the target audience.

**What to look for:**

* Simple language
* Clear headings
* Logical paragraph structure

---

### 4. Flow and UI Consistency

Checks whether instructions follow a logical and consistent order.

**What to look for:**

* Steps are ordered correctly
* No contradictory instructions
* UI and CLI flows are clearly separated

---

### 5. Specification Compliance

Checks adherence to defined agent rules and specifications.

**What to look for:**

* Follows AGENTS.md rules
* Uses required output structure
* Includes validation checklist and summary

---

### 6. Developer Experience (DX)

Checks how easy it is for a developer to follow and verify success.

**What to look for:**

* Clear success criteria
* Validation checklist present
* Minimal ambiguity

---

## Overall Grading

| Average Score | Grade |
| ------------: | ----- |
|     4.5 – 5.0 | A     |
|     4.0 – 4.4 | A-    |
|     3.5 – 3.9 | B+    |
|     3.0 – 3.4 | B     |
|     2.5 – 2.9 | C     |
|         < 2.5 | D     |

---

## Usage

* Applied by the Validation Agent
* Used to compare baseline, optimized, and refined outputs
* Results are stored as evaluation artifacts in the repository

---

## Summary

This rubric enables structured evaluation and supports iterative improvement
of AI-generated documentation through measurable criteria.
