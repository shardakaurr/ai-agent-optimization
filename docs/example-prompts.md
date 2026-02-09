# Example Prompts and Outputs

## Overview

This document provides concrete examples of reusable prompts and their corresponding outputs.
These examples demonstrate how different agents interact in the system and how documentation
improves through evaluation and refinement.

---

## Example 1: Planning New Documentation

### Input Prompt (Planning Agent)

```text
You are a Planning Agent.

Plan a beginner-friendly documentation guide for creating a GitHub repository and pushing code.

Define:
- Target audience
- Documentation type (tutorial / how-to / reference / explanation)
- High-level outline
```

### Output

* Target audience: Beginner developers
* Documentation type: Tutorial
* Outline:

  * Title
  * Overview
  * Prerequisites
  * Step-by-step instructions
  * Validation checklist
  * Summary

---

## Example 2: Writing Documentation

### Input Prompt (Authoring Agent)

```text
You are an Authoring Agent.

Write a beginner-friendly tutorial for creating a GitHub repository and pushing code.

Constraints:
- Follow the content specification
- Use GitHub-flavored Markdown
- Include a validation checklist
```

### Output

The generated documentation is stored as:

```
experiments/optimized-run-1.md
```

---

## Example 3: Documentation Evaluation

### Input Prompt (Validation Agent)

```text
You are a Validation Agent.

Evaluate the following documentation using the rubric.

Criteria:
- Accuracy
- Completeness
- Readability
- Flow/UI consistency
- Specification compliance
- Developer experience

Provide scores and improvement notes.
```

### Output

Evaluation results are recorded as:

```
results/rubric-run.md
```

---

## Example 4: Refinement Based on Evaluation

### Input Prompt (Refinement Agent)

```text
You are a Refinement Agent.

Improve the documentation using the provided evaluation feedback.
Focus on accuracy, completeness, and clarity.
```

### Output

Refined documentation is stored as:

```
experiments/optimized-run-2.md
```

---

## Reusability of Prompts

All prompts shown here are reusable across different topics by changing:

* Subject matter
* Target audience
* Documentation type

The structure and agent responsibilities remain consistent.

---

## Summary

These examples demonstrate how structured prompts and agent handoffs enable
repeatable, high-quality documentation generation and validation.
