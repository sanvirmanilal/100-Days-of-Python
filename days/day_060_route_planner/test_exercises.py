"""Behavioral checks for day 060; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_060_route_planner import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_path_cost_case_01(self):
        self.check(work.path_cost, ({'a': [('b', 4)]}, ['a', 'b']), 4,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_path_cost_case_02(self):
        self.check(work.path_cost, ({}, []), 0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_path_cost_case_03(self):
        self.check(work.path_cost, ({}, ['a', 'b']), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_dijkstra_distances_case_01(self):
        self.check(work.dijkstra_distances, ({'a': [('b', 5), ('c', 1)], 'c': [('b', 1)]}, 'a'), {'a': 0, 'c': 1, 'b': 2},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_dijkstra_distances_case_02(self):
        self.check(work.dijkstra_distances, ({}, 'x'), {'x': 0},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_dijkstra_distances_case_03(self):
        self.check(work.dijkstra_distances, ({'a': [('b', 0)], 'b': [('a', 0)]}, 'a'), {'a': 0, 'b': 0},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_cheapest_route_case_01(self):
        self.check(work.cheapest_route, ({'a': [('c', 1), ('b', 1)], 'b': [('d', 1)], 'c': [('d', 1)]}, 'a', 'd'), {'cost': 2, 'path': ['a', 'b', 'd']},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_cheapest_route_case_02(self):
        self.check(work.cheapest_route, ({}, 'x', 'x'), {'cost': 0, 'path': ['x']},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_cheapest_route_case_03(self):
        self.check(work.cheapest_route, ({}, 'x', 'y'), None,
                   mode=None, dataclass_required=False,
                   frozen=False)
