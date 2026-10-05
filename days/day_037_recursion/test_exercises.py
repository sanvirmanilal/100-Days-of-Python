"""Behavioral checks for day 037; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_037_recursion import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_factorial_case_01(self):
        self.check(work.factorial, (0,), 1,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_factorial_case_02(self):
        self.check(work.factorial, (5,), 120,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_factorial_case_03(self):
        self.check(work.factorial, (-1,), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_nested_sum_case_01(self):
        self.check(work.nested_sum, ([1, [2, [3]], []],), 6,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_nested_sum_case_02(self):
        self.check(work.nested_sum, ([],), 0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_nested_sum_case_03(self):
        self.check(work.nested_sum, (-2,), -2,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_flatten_nested_case_01(self):
        self.check(work.flatten_nested, ([1, [2, [], [3]]],), [1, 2, 3],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_flatten_nested_case_02(self):
        self.check(work.flatten_nested, ([],), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_flatten_nested_case_03(self):
        self.check(work.flatten_nested, ('x',), ['x'],
                   mode=None, dataclass_required=False,
                   frozen=False)
