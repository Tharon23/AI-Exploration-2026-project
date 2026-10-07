---
name: add-experiment
description: Standard workflow for creating, running, and recording a new AI benchmark experiment.
triggers:
  - "experiment"
  - "benchmark"
  - "run test"
  - "evaluate model"
edges:
  - target: context/conventions.md
    condition: when formatting experiment metadata
  - target: context/architecture.md
    condition: when integrating with pipeline and evaluation modules
last_updated: 2026-10-07
---

# Add Experiment Pattern

## Context
Load `context/conventions.md` to review the required experiment metadata format (course rule).

## Steps
1. Create a prompt template in `src/pipeline/prompts/<experiment_name>.txt`.
2. Define test input dataset (cases/queries) in `data/test_cases.json`.
3. Invoke model through `src/pipeline/client.py` across target models (e.g., GPT-4o, Claude 3.5, Gemini 2.5).
4. Run each test case min. 3 times to measure variance and repeatability.
5. Pipe raw outputs to `src/evaluation/scorer.py` to calculate accuracy and consistency.
6. Save results with required metadata header to `research/experiments/<exp_id>.json`.
7. Generate summary markdown table for GitLab issue Activity report.

## Gotchas
- Never pass unversioned model names (use `gpt-4o-2024-11-20`, not just `gpt-4o`).
- Always record temperature and random seed if applicable.
- Check rate limits before executing large batch runs.

## Verify
- [ ] Experiment JSON contains all required metadata fields (model, tier, version, prompt, params).
- [ ] Results include at least 3 runs per prompt to assess variance.
- [ ] Summary markdown table matches course reporting standards.

## Update Scaffold
- [ ] Update `.mex/ROUTER.md` "Current Project State" if a major benchmark phase completed.
