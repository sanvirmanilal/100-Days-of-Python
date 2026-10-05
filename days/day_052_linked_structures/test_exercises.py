"""Behavioral checks for day 052; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_052_linked_structures import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_chain_values_case_01(self):
        self.check(work.chain_values, ({'a': (1, 'b'), 'b': (2, None)}, 'a'), [1, 2],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_chain_values_case_02(self):
        self.check(work.chain_values, ({}, None), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_chain_values_case_03(self):
        self.check(work.chain_values, ({'x': (3, None)}, 'x'), [3],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_has_cycle_case_01(self):
        self.check(work.has_cycle, ({'a': (1, 'a')}, 'a'), True,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_has_cycle_case_02(self):
        self.check(work.has_cycle, ({'a': (1, None)}, 'a'), False,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_has_cycle_case_03(self):
        self.check(work.has_cycle, ({}, None), False,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_chain_intersection_case_01(self):
        self.check(work.chain_intersection, ({'a': (1, 'c'), 'b': (2, 'c'), 'c': (3, None)}, 'a', 'b'), 'c',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_chain_intersection_case_02(self):
        self.check(work.chain_intersection, ({'a': (1, None), 'b': (1, None)}, 'a', 'b'), None,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_chain_intersection_case_03(self):
        self.check(work.chain_intersection, ({}, None, None), None,
                   mode=None, dataclass_required=False,
                   frozen=False)
