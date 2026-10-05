"""Behavioral checks for day 024; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_024_dates import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_next_day_case_01(self):
        self.check(work.next_day, ('2024-02-28',), '2024-02-29',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_next_day_case_02(self):
        self.check(work.next_day, ('2023-12-31',), '2024-01-01',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_next_day_case_03(self):
        self.check(work.next_day, ('2023-02-29',), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_days_between_case_01(self):
        self.check(work.days_between, ('2024-01-01', '2024-01-03'), 2,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_days_between_case_02(self):
        self.check(work.days_between, ('2024-03-01', '2024-02-28'), -2,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_days_between_case_03(self):
        self.check(work.days_between, ('2020-01-01', '2020-01-01'), 0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_business_days_case_01(self):
        self.check(work.business_days, ('2024-01-01', '2024-01-07'), 5,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_business_days_case_02(self):
        self.check(work.business_days, ('2024-01-06', '2024-01-07'), 0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_business_days_case_03(self):
        self.check(work.business_days, ('2024-01-08', '2024-01-01'), 0,
                   mode=None, dataclass_required=False,
                   frozen=False)
