"""Behavioral checks for day 004; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_004_booleans import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_is_even_case_01(self):
        self.check(work.is_even, (2,), True,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_is_even_case_02(self):
        self.check(work.is_even, (-3,), False,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_is_even_case_03(self):
        self.check(work.is_even, (0,), True,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_in_range_case_01(self):
        self.check(work.in_range, (5, 1, 5), True,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_in_range_case_02(self):
        self.check(work.in_range, (0, 1, 5), False,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_in_range_case_03(self):
        self.check(work.in_range, (2, 2, 2), True,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_can_enter_case_01(self):
        self.check(work.can_enter, (18, True, False), True,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_can_enter_case_02(self):
        self.check(work.can_enter, (12, True, True), True,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_can_enter_case_03(self):
        self.check(work.can_enter, (30, False, True), False,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_can_enter_case_04(self):
        self.check(work.can_enter, (17, True, False), False,
                   mode=None, dataclass_required=False,
                   frozen=False)
