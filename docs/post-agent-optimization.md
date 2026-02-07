# Post-Agent Optimization Architecture

## Overview
After optimizing the AI authoring agent, the focus shifts to defining how the optimized
agent operates within a controlled content lifecycle that ensures correctness,
consistency, and good developer experience.

This document explains the end-to-end flow from prompt to validated documentation.

---

## Content Lifecycle

### 1. Prompt and Task Definition
Each documentation task starts with a clear prompt that defines:
- Topic
- Target audience
- Expected output format

Prompts are designed for GitHub-based documentation generation.

---

### 2. Planning and Outline (Specification-Driven)
Before generating content, a predefined outline is followed.
This acts as a specification and prevents unstructured output.

Standard outline:
- Title
- Overview
- Prerequisites
- Step-by-step instructions
- Validation checklist
- Summary

---

### 3. Draft Generation (Authoring Agent)
The optimized authoring agent generates the initial draft by:
- Following AGENTS.md rules
- Using a content-engineer persona
- Producing GitHub-flavored Markdown

Output artifacts are stored in:


---

### 4. Validation and Evaluation (Validation Agent)
A separate validation agent evaluates the generated content using a rubric.

Evaluation criteria include:
- Accuracy
- Completeness
- Readability
- Flow consistency
- Specification compliance

Evaluation results are documented as artifacts in:


---

### 5. Refinement and Improvement
Based on validation feedback:
- Gaps are identified
- Content is refined
- Improved versions are produced

This creates an iterative improvement loop:
Baseline → Optimized → Refined

---

## Formats and Authoring Standards
- All documentation is written in GitHub-flavored Markdown
- Commands are shown using fenced code blocks
- No executable application code is required

---

## Accuracy and Completeness Controls
Accuracy and completeness are enforced by:
- Agent rules (AGENTS.md)
- Rubric-based validation
- Explicit validation checklists in content

---

## Developer Experience
The system improves developer experience by:
- Clear step-by-step instructions
- Consistent formatting
- Validation checklists
- Reproducible documentation structure

---

## Outputs
Final outputs are validated Markdown articles that can be:
- Reviewed by humans
- Re-evaluated by agents
- Extended to automation or localization in the future

---

## Summary
Post-agent optimization, the system focuses on structured authoring,
independent validation, and iterative refinement to ensure reliable,
high-quality AI-assisted documentation.
