"""Behavioral checks for day 038; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_038_searching import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_linear_find_case_01(self):
        self.check(work.linear_find, ([3, 1, 3], 3), 0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_linear_find_case_02(self):
        self.check(work.linear_find, ([], 1), -1,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_linear_find_case_03(self):
        self.check(work.linear_find, ([1, 2], 2), 1,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_binary_find_case_01(self):
        self.check(work.binary_find, ([1, 2, 2, 4], 2), 1,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_binary_find_case_02(self):
        self.check(work.binary_find, ([], 0), -1,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_binary_find_case_03(self):
        self.check(work.binary_find, ([1, 3], 2), -1,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_binary_find_case_04(self):
        self.check(work.binary_find, ([1, 3], 3), 1,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_insertion_index_case_01(self):
        self.check(work.insertion_index, ([1, 2, 2, 4], 2), 1,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_insertion_index_case_02(self):
        self.check(work.insertion_index, ([], 3), 0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_insertion_index_case_03(self):
        self.check(work.insertion_index, ([1, 3], 9), 2,
                   mode=None, dataclass_required=False,
                   frozen=False)
