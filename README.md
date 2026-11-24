# CodeOpt

CodeOpt is a verification-first Python optimization engine. It generates candidate improvements, checks that they preserve the configured behavior on tested inputs, benchmarks the survivors, and reports the strongest supported result. It may conclude that no optimization is recommended.

## Current status

This repository is a Phase 0 / Option B scaffold. The package boundaries, contracts, test layout, corpus location, and CI checks are in place; the verifier, benchmark engine, LLM integration, sandbox, MCP adapter, and ML ranker still need implementation.

The first working slice should accept a trusted Python function through the CLI, generate or load a candidate, verify it against the original, benchmark it, and print an evidence-backed report.

## Project layout

```text
.
├── src/codeopt/
│   ├── adapters/       # CLI now; MCP and API adapters later
│   ├── core/           # Pipeline, analysis, decision, and search orchestration
│   ├── experiments/    # Run recording and future datasets
│   ├── harness/        # Comparison, verification, workloads, and benchmarks
│   ├── llm/            # Provider abstraction, prompts, and candidate schemas
│   ├── ml/             # Phase 5 feature extraction and ranking
│   ├── models/         # Stable Pydantic contracts
│   ├── sandbox/        # Trusted subprocess runner, then hardened runner
│   ├── config.py       # Application configuration
│   └── service.py      # Adapter-independent optimization entry point
├── corpus/             # Known-slow, no-improvement, and trap tasks
├── docs/adr/           # Architecture decision records
├── tests/              # Unit, integration, and sandbox tests
├── pyproject.toml      # Project metadata and tool configuration
├── requirements.txt    # pip-compatible development dependency set
└── CODEOWNERS          # Ownership map to complete before collaborative work
```

## Getting started

Use a pinned Python interpreter (Python 3.11 is the initial target) and `uv` for local environments:

```powershell
uv sync --all-groups --all-extras
uv run pytest
uv run ruff check .
```

For a pip-based environment, use `pip install -r requirements.txt`.

## Development rules

- Treat an LLM output as a hypothesis, never as proof.
- Accept a candidate only after it passes the configured comparator and exceeds a measured improvement threshold.
- Run original and candidate on identical inputs; include edge cases, mutation behavior, exceptions, ordering, types, and float tolerance in the comparison policy.
- Keep trusted local execution separate from untrusted execution. Do not run untrusted input through the local subprocess runner.
- Record environment details, timings, variance, memory measurements, and rejection reasons for every experiment.
- Keep the core independent of adapters. The CLI, MCP server, and any HTTP API call `service.optimize` rather than embedding engine logic.

## Delivery path

1. Phase 0: contracts, trusted subprocess runner, verification, benchmarking, decisions, and corpus.
2. Phase 1: LLM provider abstraction, repair loop, CLI, and a one-shot baseline.
3. Phase 2: static analysis, profiling, generated inputs, and coverage evidence.
4. Phase 3: hardened untrusted-code sandbox and budgeted multi-candidate search.
5. Phase 4: stdio MCP adapter, then a protected remote endpoint if needed.
6. Phase 5: experiment dataset and candidate ranking, only after sufficient logged data exists.

## Contract freeze at C0

Before parallel implementation begins, agree on and freeze these interfaces:

- `Task`, `Candidate`, `RunResult`, `Evidence`, `Decision`, and `Report` models.
- `Runner.run(code, entrypoint, inputs, limits) -> RunResult`.
- `service.optimize(task, budget) -> Report`.
- The corpus task format.

Changes to these contracts should receive approval from both implementation owners.
