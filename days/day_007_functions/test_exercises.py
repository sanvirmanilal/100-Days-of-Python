"""Behavioral checks for day 007; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_007_functions import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_celsius_to_fahrenheit_case_01(self):
        self.check(work.celsius_to_fahrenheit, (0,), 32.0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_celsius_to_fahrenheit_case_02(self):
        self.check(work.celsius_to_fahrenheit, (100,), 212.0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_celsius_to_fahrenheit_case_03(self):
        self.check(work.celsius_to_fahrenheit, (-40,), -40.0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_clamp_case_01(self):
        self.check(work.clamp, (5, 0, 10), 5,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_clamp_case_02(self):
        self.check(work.clamp, (-2, 0, 10), 0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_clamp_case_03(self):
        self.check(work.clamp, (12, 0, 10), 10,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_clamp_case_04(self):
        self.check(work.clamp, (1, 3, 2), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_compound_balance_case_01(self):
        self.check(work.compound_balance, (100, 0.1, 2), 121.0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_compound_balance_case_02(self):
        self.check(work.compound_balance, (50, 0.2, 0), 50,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_compound_balance_case_03(self):
        self.check(work.compound_balance, (0, 0.5, 3), 0,
                   mode=None, dataclass_required=False,
                   frozen=False)
