"""Behavioral checks for day 063; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_063_dependency_injection import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_stamp_case_01(self):
        self.check(work.stamp, ('hi', 'CALL:clock_100'), {'time': 100, 'message': 'hi'},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_stamp_case_02(self):
        self.check(work.stamp, ('', 'CALL:clock_0'), {'time': 0, 'message': ''},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_stamp_case_03(self):
        self.check(work.stamp, ('x', 'CALL:raise_value'), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_convert_prices_case_01(self):
        self.check(work.convert_prices, ([-1, 2], 'CALL:abs'), [1, 2],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_convert_prices_case_02(self):
        self.check(work.convert_prices, ([], 'CALL:abs'), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_convert_prices_case_03(self):
        self.check(work.convert_prices, ([1], 'CALL:raise_value'), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_fetch_or_default_case_01(self):
        self.check(work.fetch_or_default, ('x', 'CALL:lookup_zero', 9), 0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_fetch_or_default_case_02(self):
        self.check(work.fetch_or_default, ('missing', 'CALL:lookup_zero', 9), 9,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_fetch_or_default_case_03(self):
        self.check(work.fetch_or_default, ('x', 'CALL:raise_value', 9), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)
