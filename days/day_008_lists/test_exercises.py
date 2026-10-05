"""Behavioral checks for day 008; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_008_lists import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_double_all_case_01(self):
        self.check(work.double_all, ([1, 2, 3],), [2, 4, 6],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_double_all_case_02(self):
        self.check(work.double_all, ([],), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_double_all_case_03(self):
        self.check(work.double_all, ([-2, 0],), [-4, 0],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_positives_case_01(self):
        self.check(work.positives, ([-1, 0, 3, 2],), [3, 2],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_positives_case_02(self):
        self.check(work.positives, ([],), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_positives_case_03(self):
        self.check(work.positives, ([-4, -2],), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_running_totals_case_01(self):
        self.check(work.running_totals, ([2, 3, -1],), [2, 5, 4],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_running_totals_case_02(self):
        self.check(work.running_totals, ([],), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_running_totals_case_03(self):
        self.check(work.running_totals, ([0, 4, 0],), [0, 4, 4],
                   mode=None, dataclass_required=False,
                   frozen=False)
