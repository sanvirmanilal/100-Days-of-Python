"""Behavioral checks for day 039; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_039_complexity import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_has_duplicate_case_01(self):
        self.check(work.has_duplicate, ([1, 2, 1],), True,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_has_duplicate_case_02(self):
        self.check(work.has_duplicate, ([],), False,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_has_duplicate_case_03(self):
        self.check(work.has_duplicate, ([1, 2],), False,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_two_sum_case_01(self):
        self.check(work.two_sum, ([2, 7, 11], 9), (0, 1),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_two_sum_case_02(self):
        self.check(work.two_sum, ([3, 3], 6), (0, 1),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_two_sum_case_03(self):
        self.check(work.two_sum, ([1, 2], 9), None,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_two_sum_case_04(self):
        self.check(work.two_sum, ([1, 1, 2], 3), (0, 2),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_longest_unique_case_01(self):
        self.check(work.longest_unique, ('abcabcbb',), 3,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_longest_unique_case_02(self):
        self.check(work.longest_unique, ('',), 0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_longest_unique_case_03(self):
        self.check(work.longest_unique, ('bbbbb',), 1,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_longest_unique_case_04(self):
        self.check(work.longest_unique, ('abba',), 2,
                   mode=None, dataclass_required=False,
                   frozen=False)
