"""Behavioral checks for day 097; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_097_rate_limits import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_requests_in_window_case_01(self):
        self.check(work.requests_in_window, ([1, 3, 5, 6], 5, 3), 2,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_requests_in_window_case_02(self):
        self.check(work.requests_in_window, ([], 10, 1), 0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_requests_in_window_case_03(self):
        self.check(work.requests_in_window, ([], 0, 0), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_fixed_window_decisions_case_01(self):
        self.check(work.fixed_window_decisions, ([0, 1, 2, 5, 6], 2, 5), [True, True, False, True, True],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_fixed_window_decisions_case_02(self):
        self.check(work.fixed_window_decisions, ([0], 0, 1), [False],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_fixed_window_decisions_case_03(self):
        self.check(work.fixed_window_decisions, ([], 1, 0), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_sliding_window_decisions_case_01(self):
        self.check(work.sliding_window_decisions, ([0, 1, 2, 5, 6], 2, 5), [True, True, False, True, True],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_sliding_window_decisions_case_02(self):
        self.check(work.sliding_window_decisions, ([0, 0, 0], 1, 5), [True, False, False],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_sliding_window_decisions_case_03(self):
        self.check(work.sliding_window_decisions, ([], 1, 0), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)
