# 100 Days of Python

A complete, self-paced curriculum: **100 distinct days, 300 exercises**, and a project every tenth day. Start with values and loops; finish with data pipelines, concurrency, and a workflow engine.

Each day contains a short lesson, runnable worked examples, and three increasingly demanding exercises: **foundation → application → stretch**. The exercise files contain `NotImplementedError` stubs, never solutions. Worked examples demonstrate the topic independently of the assignments.

## Start here

Use **Python 3.11 or newer**. Everything uses the standard library; there are no packages to install and no API keys, network services, or paid tools to configure.

Run commands from this repository folder. An optional virtual environment keeps your work isolated:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python practice.py --check
python practice.py 1 --examples
python practice.py 1 --exercise 1
```

Open [day 001](days/day_001_values/README.md), then edit its `exercises.py`. The first test run should fail with `NotImplementedError`: that means the exercise has not been attempted yet. Implement the requested behavior and rerun its checks.

## Daily routine

1. Read the day's lesson and predict the worked example's output before running it.
2. Experiment with the examples, then write down each exercise's inputs, outputs, and boundaries.
3. Implement the foundation exercise, run its tests, and explain any failure before changing code.
4. Continue to application and stretch. You may add private helper functions and classes in `exercises.py`.
5. Add your own tests in `test_exercises.py`, especially for a boundary the supplied cases omit.
6. Record your reasoning and questions using [the journal template](JOURNAL_TEMPLATE.md). Request a hint or review after an attempt.

```powershell
python practice.py 12                 # Test all three exercises for day 12
python practice.py 12 --exercise 2    # Focus on the application exercise
python practice.py 12 --examples      # Run only the independent worked examples
python practice.py --progress         # Grade all attempts; show PASS/TODO per exercise
python practice.py --check            # Verify curriculum structure; does not grade your knowledge
```

Tests can also run directly:

```powershell
python -m unittest days.day_001_values.test_exercises -v
python -m unittest discover -s days -p test_exercises.py -t .
```

The full exercise suite will fail for unfinished days. `--progress` summarizes those failures without hundreds of tracebacks and exits successfully as a reporting command. Individual grading commands exit nonzero on failure. Progress is calculated from current code; no separate completion file needs updating.

## What the tests prove

Each exercise has multiple concrete cases, including edge cases and invalid inputs where specified. Checks also cover caller-owned input preservation, iterator and coroutine contracts, and selected stateful behavior. Files use temporary UTF-8 fixtures; SQLite uses in-memory connections; random exercises use local seeds.

A passing test suite establishes the tested behavior, not complete mastery. Some requirements—such as using binary search, avoiding `eval`, algorithmic complexity, readable design, true laziness, and robust thread safety—also need code review and your explanation. Add meaningful cases rather than editing expected results to fit your code.

## Layout

```text
CURRICULUM.md                 All 100 days in learning order
days/day_NNN_topic/
    README.md                 Lesson, exercise contracts, reflection prompts
    examples.py               Runnable worked learning examples
    exercises.py              Your attempts; initially unfinished stubs
    test_exercises.py         Tests and expected behavior, no implementations
practice.py                   Examples, grading, progress, and integrity checks
tests/                        Shared fixtures and repository integrity checks
tools/build_curriculum.py     Curriculum authoring data and generator
JOURNAL_TEMPLATE.md            Copy for your daily reflection
```

See [the complete curriculum](CURRICULUM.md). Days build on earlier concepts but keep their own code; later days do not import your earlier attempts.

## Hints and solutions after attempts

No solution bank is included. After trying an exercise, share your attempt, failing test, and reasoning, then ask for a small hint, code review, or a solution comparison. Commit your attempt before any later solution so you can compare the approaches. See [contribution guidance](CONTRIBUTING.md).

The curriculum generator is for maintaining the scaffold, not daily practice. It refuses to replace existing days unless you explicitly pass `--overwrite`. **That option overwrites all day files, including attempts and learner-added tests.** Use it only in a separate clean checkout or after deliberately backing up your work. Do not run it as part of setup.
