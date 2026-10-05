"""Behavioral checks for day 059; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_059_dynamic_programming import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_fibonacci_case_01(self):
        self.check(work.fibonacci, (0,), 0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_fibonacci_case_02(self):
        self.check(work.fibonacci, (10,), 55,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_fibonacci_case_03(self):
        self.check(work.fibonacci, (30,), 832040,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_min_coins_case_01(self):
        self.check(work.min_coins, ([1, 3, 4], 6), 2,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_min_coins_case_02(self):
        self.check(work.min_coins, ([2], 3), None,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_min_coins_case_03(self):
        self.check(work.min_coins, ([], 0), 0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_edit_distance_case_01(self):
        self.check(work.edit_distance, ('kitten', 'sitting'), 3,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_edit_distance_case_02(self):
        self.check(work.edit_distance, ('', 'abc'), 3,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_edit_distance_case_03(self):
        self.check(work.edit_distance, ('same', 'same'), 0,
                   mode=None, dataclass_required=False,
                   frozen=False)
