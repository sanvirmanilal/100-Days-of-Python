"""Behavioral checks for day 009; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_009_dictionaries import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_lookup_case_01(self):
        self.check(work.lookup, ({'a': 1}, 'a', 0), 1,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_lookup_case_02(self):
        self.check(work.lookup, ({}, 'x', 7), 7,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_lookup_case_03(self):
        self.check(work.lookup, ({'a': None}, 'a', 5), None,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_frequencies_case_01(self):
        self.check(work.frequencies, (['a', 'b', 'a'],), {'a': 2, 'b': 1},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_frequencies_case_02(self):
        self.check(work.frequencies, ([],), {},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_frequencies_case_03(self):
        self.check(work.frequencies, ([1, 1, 2],), {1: 2, 2: 1},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_merge_totals_case_01(self):
        self.check(work.merge_totals, ({'a': 2}, {'a': 3, 'b': 1}), {'a': 5, 'b': 1},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_merge_totals_case_02(self):
        self.check(work.merge_totals, ({}, {}), {},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_merge_totals_case_03(self):
        self.check(work.merge_totals, ({'x': -2}, {'x': 2}), {'x': 0},
                   mode=None, dataclass_required=False,
                   frozen=False)
