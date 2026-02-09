# Custom Agents, Skills, and Handoffs

## Overview

This document defines custom agents, their responsibilities, skills, and how work is handed off between them.
The goal is to avoid single-agent overload and ensure clear accountability.

---

## Agent Definitions

### 1. Planning Agent

**Purpose:** Plan new documentation.

Responsibilities:

* Define documentation goals
* Identify target audience
* Select documentation type (tutorial, how-to, reference, explanation)

Outputs:

* Outline
* Content plan

---

### 2. Gap Assessment Agent

**Purpose:** Assess gaps in existing documentation.

Responsibilities:

* Review baseline documentation
* Identify missing steps or unclear sections
* Flag accuracy risks

Outputs:

* Gap assessment notes

---

### 3. Authoring Agent

**Purpose:** Write documentation content.

Responsibilities:

* Generate documentation drafts
* Follow `content-spec.md`
* Use GitHub-flavored Markdown

Outputs:

* Draft documentation in `experiments/`

---

### 4. Validation Agent

**Purpose:** Evaluate documentation quality.

Responsibilities:

* Apply rubric-based evaluation
* Score accuracy, completeness, and DX
* Produce evaluation artifacts

Outputs:

* Rubric scores in `results/`

---

### 5. Refinement Agent

**Purpose:** Improve documentation based on evaluation results.

Responsibilities:

* Apply approved feedback
* Improve clarity and completeness
* Produce refined versions

Outputs:

* Optimized documentation runs

---

## Agent Handoff Flow

```
Planning → Gap Assessment → Authoring → Validation → Refinement
```

Each agent operates independently and hands off outputs to the next stage.

---

## Agent Skills

| Skill Area        | Used By          |
| ----------------- | ---------------- |
| Evaluation        | Validation Agent |
| Content Discovery | Planning Agent   |
| SDK Knowledge     | Authoring Agent  |
| Code Testing      | Validation Agent |
| Vision (Future)   | Validation Agent |

---

## Summary

This multi-agent design avoids single-agent responsibility overload and enables scalable, reusable documentation workflows.
