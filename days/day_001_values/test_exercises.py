"""Behavioral checks for day 001; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_001_values import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_greet_case_01(self):
        self.check(work.greet, ('Ada',), 'Hello, Ada!',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_greet_case_02(self):
        self.check(work.greet, ('',), 'Hello, !',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_greet_case_03(self):
        self.check(work.greet, ('Lin Chen',), 'Hello, Lin Chen!',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_describe_case_01(self):
        self.check(work.describe, ('Ada', 36), 'Ada is 36 years old.',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_describe_case_02(self):
        self.check(work.describe, ('Bo', 0), 'Bo is 0 years old.',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_describe_case_03(self):
        self.check(work.describe, ('Cy', 101), 'Cy is 101 years old.',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_swap_values_case_01(self):
        self.check(work.swap_values, (1, 2), (2, 1),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_swap_values_case_02(self):
        self.check(work.swap_values, ('x', None), (None, 'x'),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_swap_values_case_03(self):
        self.check(work.swap_values, (True, 3), (3, True),
                   mode=None, dataclass_required=False,
                   frozen=False)
