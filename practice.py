"""Run examples, exercise checks, or a progress snapshot from the repository root."""
import argparse
import importlib
import io
from pathlib import Path
import runpy
import sys
import unittest

ROOT = Path(__file__).resolve().parent


def day_folders():
    return sorted((ROOT / 'days').glob('day_[0-9][0-9][0-9]_*'))


def suite_for(folder, exercise=None):
    module = importlib.import_module(f'days.{folder.name}.test_exercises')
    suite = unittest.defaultTestLoader.loadTestsFromModule(module)
    if exercise is None:
        return suite
    return unittest.TestSuite(test for group in suite for test in group
                              if test._testMethodName.startswith(f'test_{exercise:02d}_'))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('day', nargs='?', type=int, help='Day 1 through 100')
    parser.add_argument('--exercise', type=int, choices=[1, 2, 3], help='Test one exercise')
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument('--examples', action='store_true', help='Run worked examples for the chosen day')
    modes.add_argument('--progress', action='store_true', help='Run all checks and summarize completed exercises')
    modes.add_argument('--check', action='store_true', help='Check repository structure without grading attempts')
    args = parser.parse_args(argv)
    if args.exercise and (args.examples or args.progress or args.check):
        parser.error('--exercise is only used when testing a day')
    if (args.progress or args.check) and args.day is not None:
        parser.error('--progress and --check do not take a day')
    if args.check:
        result = unittest.TextTestRunner(verbosity=2).run(
            unittest.defaultTestLoader.discover(str(ROOT / 'tests'), pattern='test_*.py', top_level_dir=str(ROOT)))
        return 0 if result.wasSuccessful() else 1
    folders = day_folders()
    if args.progress:
        completed = 0
        for number, folder in enumerate(folders, 1):
            statuses = []
            for level in range(1, 4):
                result = unittest.TextTestRunner(stream=io.StringIO()).run(suite_for(folder, level))
                passed = result.testsRun > 0 and result.wasSuccessful()
                completed += passed
                statuses.append('PASS' if passed else 'TODO')
            print(f'Day {number:03d}: ' + ' | '.join(statuses))
        print(f'\n{completed}/300 exercises passing. PASS means supplied checks passed; add your own tests too.')
        return 0
    if args.day is None or not 1 <= args.day <= 100:
        parser.error('Choose a day from 1 through 100, or use --progress / --check')
    folder = folders[args.day - 1]
    if args.examples:
        runpy.run_path(str(folder / 'examples.py'), run_name='__main__')
        return 0
    result = unittest.TextTestRunner(verbosity=2).run(suite_for(folder, args.exercise))
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    sys.exit(main())
