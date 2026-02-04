# Automated Validation Using AI Agents in CI/CD

## Overview
This project extends manual evaluation into an automated validation workflow using AI agents.
The goal is to ensure that user guides are validated consistently, objectively, and repeatably as part of a CI/CD pipeline.

---

## Automated Validation Agent
An automated validation agent is responsible for evaluating documentation whenever changes are made.

The agent performs:
- Rule-based validation using AGENTS.md
- Content evaluation using a secondary LLM
- Optional tool-based checks via MCP (e.g., Playwright)

---

## CI/CD Workflow Integration
The validation agent is designed to run automatically within a CI/CD pipeline (e.g., GitHub Actions).

### Trigger
- Documentation updates
- Changes to agent rules or specifications

### Pipeline Flow
1. CI/CD pipeline starts
2. Validation agent is invoked
3. Validation checks are executed
4. A rubric-based assessment is generated
5. A score and feedback report is produced

---

## Tool-Based Validation with Playwright MCP
Using MCP, the validation agent can invoke Playwright to:
- Open referenced web pages
- Verify the presence of UI elements
- Detect gaps where instructions do not match the actual interface

This enables partial execution-based validation of instructions.

---

## Cross-LLM Content Evaluation
A secondary LLM is used as an independent reviewer to evaluate:
- Clarity and readability
- Completeness of steps
- Ambiguity and hallucination risk

This reduces reliance on a single model and improves evaluation robustness.

---

## Automated Validation Rubric
The validation agent automatically completes a human-readable rubric.

### Example Rubric

Criteria | Score (1–5) | Notes
-------- | ------------ | -----
Instruction Accuracy |  | 
Completeness |  | 
Readability |  | 
UI Consistency |  | 
Specification Compliance |  | 

### Output
- Overall Score (percentage)
- Grade (A/B/C/D)
- Actionable feedback

---

## Benefits of Automation
- Consistent quality checks
- Reduced manual effort
- Early detection of issues
- Reproducible evaluation results

---

## Summary
This automated validation design transforms AI-generated documentation evaluation into a scalable CI/CD process, enabling reliable quality gates for AI-assisted content creation.
