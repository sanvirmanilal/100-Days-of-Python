"""Behavioral checks for day 093; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_093_sorting_algorithms import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_insertion_sort_case_01(self):
        self.check(work.insertion_sort, ([3, 1, 2],), [1, 2, 3],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_insertion_sort_case_02(self):
        self.check(work.insertion_sort, ([],), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_insertion_sort_case_03(self):
        self.check(work.insertion_sort, ([2, 2, -1],), [-1, 2, 2],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_merge_sort_case_01(self):
        self.check(work.merge_sort, ([4, 1, 3, 2],), [1, 2, 3, 4],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_merge_sort_case_02(self):
        self.check(work.merge_sort, ([],), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_merge_sort_case_03(self):
        self.check(work.merge_sort, ([3, 3, 1],), [1, 3, 3],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_count_inversions_case_01(self):
        self.check(work.count_inversions, ([3, 1, 2],), 2,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_count_inversions_case_02(self):
        self.check(work.count_inversions, ([],), 0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_count_inversions_case_03(self):
        self.check(work.count_inversions, ([2, 2, 1],), 2,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_count_inversions_case_04(self):
        self.check(work.count_inversions, ([4, 3, 2, 1],), 6,
                   mode=None, dataclass_required=False,
                   frozen=False)
