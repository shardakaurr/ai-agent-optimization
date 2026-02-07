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
