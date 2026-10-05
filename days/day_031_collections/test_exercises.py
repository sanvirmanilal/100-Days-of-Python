"""Behavioral checks for day 031; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_031_collections import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_most_common_case_01(self):
        self.check(work.most_common, (['b', 'a', 'b', 'a', 'c'], 2), [('a', 2), ('b', 2)],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_most_common_case_02(self):
        self.check(work.most_common, ([], 3), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_most_common_case_03(self):
        self.check(work.most_common, (['x'], 0), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_group_lengths_case_01(self):
        self.check(work.group_lengths, (['a', 'bb', 'c'],), {1: ['a', 'c'], 2: ['bb']},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_group_lengths_case_02(self):
        self.check(work.group_lengths, ([],), {},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_group_lengths_case_03(self):
        self.check(work.group_lengths, (['', ''],), {0: ['', '']},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_inventory_difference_case_01(self):
        self.check(work.inventory_difference, (['a', 'a', 'b'], ['a', 'c']), {'a': -1, 'b': -1, 'c': 1},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_inventory_difference_case_02(self):
        self.check(work.inventory_difference, ([], []), {},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_inventory_difference_case_03(self):
        self.check(work.inventory_difference, (['x'], ['x', 'x']), {'x': 1},
                   mode=None, dataclass_required=False,
                   frozen=False)
