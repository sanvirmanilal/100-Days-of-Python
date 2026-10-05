"""Behavioral checks for day 054; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_054_binary_search_trees import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_bst_contains_case_01(self):
        self.check(work.bst_contains, ((2, (1, None, None), (3, None, None)), 3), True,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_bst_contains_case_02(self):
        self.check(work.bst_contains, (None, 1), False,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_bst_contains_case_03(self):
        self.check(work.bst_contains, ((2, None, None), 1), False,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_bst_min_case_01(self):
        self.check(work.bst_min, ((3, (1, None, (2, None, None)), None),), 1,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_bst_min_case_02(self):
        self.check(work.bst_min, (None,), None,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_bst_min_case_03(self):
        self.check(work.bst_min, ((0, None, None),), 0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_is_bst_case_01(self):
        self.check(work.is_bst, ((2, (1, None, None), (3, None, None)),), True,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_is_bst_case_02(self):
        self.check(work.is_bst, ((5, (3, None, (6, None, None)), None),), False,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_is_bst_case_03(self):
        self.check(work.is_bst, ((1, (1, None, None), None),), False,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_is_bst_case_04(self):
        self.check(work.is_bst, (None,), True,
                   mode=None, dataclass_required=False,
                   frozen=False)
