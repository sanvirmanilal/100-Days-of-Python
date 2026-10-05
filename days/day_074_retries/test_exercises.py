"""Behavioral checks for day 074; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_074_retries import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_backoff_case_01(self):
        self.check(work.backoff, (1, 4), [1, 2, 4, 8],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_backoff_case_02(self):
        self.check(work.backoff, (0.5, 0), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_backoff_case_03(self):
        self.check(work.backoff, (-1, 2), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_retryable_case_01(self):
        self.check(work.retryable, (429,), True,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_retryable_case_02(self):
        self.check(work.retryable, (503,), True,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_retryable_case_03(self):
        self.check(work.retryable, (404,), False,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_first_success_case_01(self):
        self.check(work.first_success, ([500, 200], 3), 2,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_first_success_case_02(self):
        self.check(work.first_success, ([404, 200], 3), None,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_first_success_case_03(self):
        self.check(work.first_success, ([500, 200], 1), None,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_first_success_case_04(self):
        self.check(work.first_success, ([], 0), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)
