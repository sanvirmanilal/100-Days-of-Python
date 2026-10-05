"""Behavioral checks for day 033; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_033_iterators import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_first_or_case_01(self):
        self.check(work.first_or, ([1, 2],), 1,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_first_or_case_02(self):
        self.check(work.first_or, ([],), None,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_first_or_case_03(self):
        self.check(work.first_or, ([], 7), 7,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_take_case_01(self):
        self.check(work.take, ([1, 2, 3], 2), [1, 2],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_take_case_02(self):
        self.check(work.take, ([], 3), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_take_case_03(self):
        self.check(work.take, ([1, 2], 0), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_pairwise_case_01(self):
        self.check(work.pairwise, ([1, 2, 3],), [(1, 2), (2, 3)],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_pairwise_case_02(self):
        self.check(work.pairwise, ([],), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_pairwise_case_03(self):
        self.check(work.pairwise, ([1],), [],
                   mode=None, dataclass_required=False,
                   frozen=False)
