"""Behavioral checks for day 085; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_085_windows import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_window_sums_case_01(self):
        self.check(work.window_sums, ([1, 2, 3, 4], 2), [3, 5, 7],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_window_sums_case_02(self):
        self.check(work.window_sums, ([1], 2), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_window_sums_case_03(self):
        self.check(work.window_sums, ([], 0), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_moving_average_case_01(self):
        self.check(work.moving_average, ([2, 4, 6], 2), [3.0, 5.0],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_moving_average_case_02(self):
        self.check(work.moving_average, ([], 1), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_moving_average_case_03(self):
        self.check(work.moving_average, ([1], 0), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_window_maxima_case_01(self):
        self.check(work.window_maxima, ([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_window_maxima_case_02(self):
        self.check(work.window_maxima, ([2, 2], 1), [2, 2],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_window_maxima_case_03(self):
        self.check(work.window_maxima, ([], 0), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)
