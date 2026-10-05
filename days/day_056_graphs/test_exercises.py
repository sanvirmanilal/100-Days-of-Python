"""Behavioral checks for day 056; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_056_graphs import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_neighbors_case_01(self):
        self.check(work.neighbors, ({'a': ['b', 'c']}, 'a'), ['b', 'c'],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_neighbors_case_02(self):
        self.check(work.neighbors, ({}, 'a'), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_neighbors_case_03(self):
        self.check(work.neighbors, ({'a': []}, 'a'), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_reachable_case_01(self):
        self.check(work.reachable, ({'a': ['b'], 'b': ['a', 'c']}, 'a'), {'a', 'b', 'c'},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_reachable_case_02(self):
        self.check(work.reachable, ({}, 'x'), {'x'},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_reachable_case_03(self):
        self.check(work.reachable, ({'a': [], 'b': ['a']}, 'a'), {'a'},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_has_path_case_01(self):
        self.check(work.has_path, ({'a': ['b']}, 'a', 'b'), True,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_has_path_case_02(self):
        self.check(work.has_path, ({}, 'x', 'x'), True,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_has_path_case_03(self):
        self.check(work.has_path, ({'a': ['b']}, 'b', 'a'), False,
                   mode=None, dataclass_required=False,
                   frozen=False)
