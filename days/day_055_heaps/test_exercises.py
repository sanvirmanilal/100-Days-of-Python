"""Behavioral checks for day 055; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_055_heaps import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_smallest_case_01(self):
        self.check(work.smallest, ([5, 1, 3, 1], 3), [1, 1, 3],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_smallest_case_02(self):
        self.check(work.smallest, ([], 2), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_smallest_case_03(self):
        self.check(work.smallest, ([1], 0), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_schedule_jobs_case_01(self):
        self.check(work.schedule_jobs, ([(2, 'b'), (1, 'c'), (1, 'a')],), ['a', 'c', 'b'],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_schedule_jobs_case_02(self):
        self.check(work.schedule_jobs, ([],), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_schedule_jobs_case_03(self):
        self.check(work.schedule_jobs, ([(0, 'x'), (0, 'x')],), ['x', 'x'],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_merge_sorted_case_01(self):
        self.check(work.merge_sorted, ([[1, 4], [2, 3], []],), [1, 2, 3, 4],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_merge_sorted_case_02(self):
        self.check(work.merge_sorted, ([],), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_merge_sorted_case_03(self):
        self.check(work.merge_sorted, ([[1, 1], [1]],), [1, 1, 1],
                   mode=None, dataclass_required=False,
                   frozen=False)
