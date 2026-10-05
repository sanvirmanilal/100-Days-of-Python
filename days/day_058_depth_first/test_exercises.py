"""Behavioral checks for day 058; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_058_depth_first import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_dfs_order_case_01(self):
        self.check(work.dfs_order, ({'a': ['b', 'c'], 'b': ['d']}, 'a'), ['a', 'b', 'd', 'c'],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_dfs_order_case_02(self):
        self.check(work.dfs_order, ({}, 'x'), ['x'],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_dfs_order_case_03(self):
        self.check(work.dfs_order, ({'a': ['a']}, 'a'), ['a'],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_directed_cycle_case_01(self):
        self.check(work.directed_cycle, ({'a': ['b'], 'b': ['a']},), True,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_directed_cycle_case_02(self):
        self.check(work.directed_cycle, ({'a': ['b']},), False,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_directed_cycle_case_03(self):
        self.check(work.directed_cycle, ({},), False,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_topological_order_case_01(self):
        self.check(work.topological_order, ({'a': ['c'], 'b': ['c']},), ['a', 'b', 'c'],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_topological_order_case_02(self):
        self.check(work.topological_order, ({},), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_topological_order_case_03(self):
        self.check(work.topological_order, ({'a': ['b'], 'b': ['a']},), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)
