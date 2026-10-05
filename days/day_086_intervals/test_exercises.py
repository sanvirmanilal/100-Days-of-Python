"""Behavioral checks for day 086; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_086_intervals import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_overlap_case_01(self):
        self.check(work.overlap, ((1, 3), (2, 4)), True,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_overlap_case_02(self):
        self.check(work.overlap, ((1, 2), (2, 3)), False,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_overlap_case_03(self):
        self.check(work.overlap, ((0, 1), (3, 4)), False,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_merge_intervals_case_01(self):
        self.check(work.merge_intervals, ([(3, 5), (1, 3), (8, 9)],), [(1, 5), (8, 9)],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_merge_intervals_case_02(self):
        self.check(work.merge_intervals, ([],), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_merge_intervals_case_03(self):
        self.check(work.merge_intervals, ([(1, 4), (2, 3)],), [(1, 4)],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_max_concurrent_case_01(self):
        self.check(work.max_concurrent, ([(1, 3), (2, 4), (3, 5)],), 2,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_max_concurrent_case_02(self):
        self.check(work.max_concurrent, ([],), 0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_max_concurrent_case_03(self):
        self.check(work.max_concurrent, ([(1, 2), (2, 3)],), 1,
                   mode=None, dataclass_required=False,
                   frozen=False)
