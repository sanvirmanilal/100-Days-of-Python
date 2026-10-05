"""Integrity checks, separate from tests that grade learner attempts."""
import ast
import importlib
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class RepositoryTests(unittest.TestCase):
    def test_exactly_100_sequential_days(self):
        folders = sorted((ROOT / 'days').glob('day_[0-9][0-9][0-9]_*'))
        self.assertEqual(len(folders), 100)
        self.assertEqual([folder.name[4:7] for folder in folders], [f'{day:03d}' for day in range(1, 101)])

    def test_each_day_has_lessons_examples_and_checks(self):
        for folder in sorted((ROOT / 'days').glob('day_*')):
            with self.subTest(day=folder.name):
                for name in ['README.md', 'examples.py', 'exercises.py', 'test_exercises.py', '__init__.py']:
                    self.assertTrue((folder / name).is_file(), name)
                lesson = (folder / 'README.md').read_text(encoding='utf-8')
                self.assertIn('## Learn', lesson)
                for level in ['Foundation', 'Application', 'Stretch']:
                    self.assertIn(level, lesson)

    def test_all_python_sources_parse(self):
        for folder_name in ['days', 'tests', 'tools']:
            for path in (ROOT / folder_name).rglob('*.py'):
                with self.subTest(file=str(path.relative_to(ROOT))):
                    ast.parse(path.read_text(encoding='utf-8'), filename=str(path))
        ast.parse((ROOT / 'practice.py').read_text(encoding='utf-8'))

    def test_three_exercises_with_multiple_test_cases(self):
        for folder in sorted((ROOT / 'days').glob('day_*')):
            with self.subTest(day=folder.name):
                module = importlib.import_module(f'days.{folder.name}.test_exercises')
                names = unittest.defaultTestLoader.getTestCaseNames(module.ExerciseTests)
                for level in range(1, 4):
                    self.assertGreaterEqual(sum(name.startswith(f'test_{level:02d}_') for name in names), 3)
                self.assertTrue(all(name.startswith(('test_01_', 'test_02_', 'test_03_')) for name in names))

    def test_curriculum_links_resolve(self):
        import re
        curriculum = (ROOT / 'CURRICULUM.md').read_text(encoding='utf-8')
        links = re.findall(r'\]\((days/[^)]+)\)', curriculum)
        self.assertEqual(len(links), 100)
        for link in links:
            self.assertTrue((ROOT / link).is_file(), link)
