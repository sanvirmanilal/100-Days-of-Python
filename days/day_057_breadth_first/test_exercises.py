"""Behavioral checks for day 057; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_057_breadth_first import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_bfs_order_case_01(self):
        self.check(work.bfs_order, ({'a': ['b', 'c'], 'b': ['c']}, 'a'), ['a', 'b', 'c'],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_bfs_order_case_02(self):
        self.check(work.bfs_order, ({}, 'x'), ['x'],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_bfs_order_case_03(self):
        self.check(work.bfs_order, ({'a': ['a']}, 'a'), ['a'],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_distances_case_01(self):
        self.check(work.distances, ({'a': ['b', 'c'], 'b': ['d'], 'c': ['d']}, 'a'), {'a': 0, 'b': 1, 'c': 1, 'd': 2},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_distances_case_02(self):
        self.check(work.distances, ({}, 'x'), {'x': 0},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_distances_case_03(self):
        self.check(work.distances, ({'a': ['b'], 'b': ['a']}, 'a'), {'a': 0, 'b': 1},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_shortest_path_case_01(self):
        self.check(work.shortest_path, ({'a': ['b', 'c'], 'b': ['d'], 'c': ['d']}, 'a', 'd'), ['a', 'b', 'd'],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_shortest_path_case_02(self):
        self.check(work.shortest_path, ({}, 'x', 'x'), ['x'],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_shortest_path_case_03(self):
        self.check(work.shortest_path, ({}, 'x', 'y'), None,
                   mode=None, dataclass_required=False,
                   frozen=False)
