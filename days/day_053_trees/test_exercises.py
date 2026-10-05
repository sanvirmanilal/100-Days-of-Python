"""Behavioral checks for day 053; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_053_trees import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_tree_size_case_01(self):
        self.check(work.tree_size, (None,), 0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_tree_size_case_02(self):
        self.check(work.tree_size, ((1, None, None),), 1,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_tree_size_case_03(self):
        self.check(work.tree_size, ((2, (1, None, None), (3, None, None)),), 3,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_tree_height_case_01(self):
        self.check(work.tree_height, (None,), 0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_tree_height_case_02(self):
        self.check(work.tree_height, ((1, None, None),), 1,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_tree_height_case_03(self):
        self.check(work.tree_height, ((1, (2, (3, None, None), None), None),), 3,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_inorder_case_01(self):
        self.check(work.inorder, ((2, (1, None, None), (3, None, None)),), [1, 2, 3],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_inorder_case_02(self):
        self.check(work.inorder, (None,), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_inorder_case_03(self):
        self.check(work.inorder, ((1, None, (2, None, None)),), [1, 2],
                   mode=None, dataclass_required=False,
                   frozen=False)
