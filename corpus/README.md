# Evaluation corpus

Store one self-contained task per file or subdirectory, with its original implementation, expected behavior, representative inputs, and any approved variants.

The first corpus should include 10–15 tasks:

- Known-slow cases with safe improvements.
- No-improvement cases where the correct result is `NO_IMPROVEMENT`.
- Trap cases where a plausible optimization changes ordering, duplicates, mutation, exceptions, or another boundary behavior.

Keep an evaluation split separate from development tasks once the corpus grows. The exact corpus format is a C0 contract and is intentionally not fixed by this scaffold.
