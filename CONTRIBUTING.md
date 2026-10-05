# Keeping the learning process useful

Exercise contracts live in each day's README and stub docstrings. Supplied tests make those contracts concrete; add tests for meaningful gaps while preserving their stated behavior.

Name learner-added tests `test_01_description`, `test_02_description`, or `test_03_description` to associate them with foundation, application, or stretch. The single-exercise runner and progress report use those prefixes. Other `test_` methods run in the full-day suite only.

Commit attempts before asking for a solution comparison. Keep mistakes and reasoning in your journal so later review shows what you learned. This repository intentionally starts without exercise solutions.

When requesting help, include the day and exercise, your attempted code, the exact failing test, and what you expected. Ask first for the smallest useful hint. Full solutions can be added later after attempts, when explicitly requested.

Curriculum maintainers: `tools/build_curriculum.py` holds topics, contracts, worked examples, and expected cases. It contains no assignment implementations. Generation overwrites learner files; work in a clean checkout, review the generated diff, run `python practice.py --check`, and run every worked example. Preserve learner changes before regenerating. Structural checks do not validate all expected answers; review changes to test data as carefully as code.
