"""Behavioral checks for day 013; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_013_sets import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_unique_count_case_01(self):
        self.check(work.unique_count, ([1, 1, 2],), 2,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_unique_count_case_02(self):
        self.check(work.unique_count, ([],), 0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_unique_count_case_03(self):
        self.check(work.unique_count, (['a', 'A'],), 2,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_common_items_case_01(self):
        self.check(work.common_items, ([1, 2], [2, 3]), {2},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_common_items_case_02(self):
        self.check(work.common_items, ([], [1]), set(),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_common_items_case_03(self):
        self.check(work.common_items, (['x', 'x'], ['x']), {'x'},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_missing_numbers_case_01(self):
        self.check(work.missing_numbers, ([1, 3], 4), [2, 4],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_missing_numbers_case_02(self):
        self.check(work.missing_numbers, ([], 0), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_missing_numbers_case_03(self):
        self.check(work.missing_numbers, ([0, 1, 1, 9], 3), [2, 3],
                   mode=None, dataclass_required=False,
                   frozen=False)
