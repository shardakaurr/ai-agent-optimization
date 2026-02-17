# Setup and Run Guide

## Overview

This document provides clear instructions for setting up and interacting with the AI Agent Optimization project using CLI-style prompts and a web-based documentation experience.

The goal is to keep the main README concise while offering detailed setup steps for reviewers and users.

---

## Prerequisites

* Git installed
* GitHub account
* Visual Studio Code
* GitHub Copilot Chat extension enabled

---

## Repository Setup

1. Clone the repository:

```bash
git clone https://github.com/shardakaurr/ai-agent-optimization.git
```

2. Open the project in VS Code:

```bash
code ai-agent-optimization
```

3. Ensure GitHub Copilot Chat is active in VS Code.

---

## CLI-Style Interaction (Agent Execution)

This project simulates CLI interactions through structured prompts in Copilot Chat.

Example interactions:

```text
generate-docs --agent authoring --input specs/content-spec.md
```

```text
validate-docs --agent validation --rubric docs/rubric.md
```

These commands represent how users conceptually interact with different agents.

---

## Web UI Interaction (Documentation Experience)

The web interface is represented by rendered Markdown files in GitHub.

To view generated outputs:

* Open files in the `experiments/` folder
* View evaluation results in `results/rubric-run.md`
* Read walkthrough documentation in `docs/blog_post.md`

This provides a UI-like experience without requiring a separate application.

---

## Running the Validation Workflow

1. Open an experiment file (baseline or optimized run).
2. Use Copilot Chat as the Validation Agent.
3. Apply scoring based on `docs/rubric.md`.
4. Record results in `results/rubric-run.md`.

---

## Summary

The project uses a documentation-first workflow where CLI-style prompts drive agent execution and GitHub Markdown acts as the viewing interface. This setup keeps the system simple while demonstrating scalable interaction models.
