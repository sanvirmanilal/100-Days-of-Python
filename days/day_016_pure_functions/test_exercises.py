"""Behavioral checks for day 016; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_016_pure_functions import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_increment_all_case_01(self):
        self.check(work.increment_all, ([1, 2], 3), [4, 5],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_increment_all_case_02(self):
        self.check(work.increment_all, ([], 5), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_increment_all_case_03(self):
        self.check(work.increment_all, ([0], -1), [-1],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_with_setting_case_01(self):
        self.check(work.with_setting, ({'a': 1}, 'b', 2), {'a': 1, 'b': 2},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_with_setting_case_02(self):
        self.check(work.with_setting, ({}, 'a', None), {'a': None},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_with_setting_case_03(self):
        self.check(work.with_setting, ({'a': 1}, 'a', 3), {'a': 3},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_normalize_scores_case_01(self):
        self.check(work.normalize_scores, ([2, 4],), [0.5, 1.0],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_normalize_scores_case_02(self):
        self.check(work.normalize_scores, ([],), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_normalize_scores_case_03(self):
        self.check(work.normalize_scores, ([0, 0],), [0, 0],
                   mode=None, dataclass_required=False,
                   frozen=False)
