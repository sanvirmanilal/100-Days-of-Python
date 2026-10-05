"""Behavioral checks for day 044; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_044_properties import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_Temperature_case_01(self):
        self.check(work.Temperature, (0,), ObjectChecks([('@fahrenheit', (), 32.0), ('set_celsius', (100,), None), ('@fahrenheit', (), 212.0)]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_Temperature_case_02(self):
        self.check(work.Temperature, (-273.15,), ObjectChecks([('@celsius', (), -273.15), ('set_celsius', (-300,), ValueError), ('@celsius', (), -273.15)]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_Temperature_case_03(self):
        self.check(work.Temperature, (-300,), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_BoundedCounter_case_01(self):
        self.check(work.BoundedCounter, (2,), ObjectChecks([('increment', (), 1), ('increment', (), 2), ('increment', (), ValueError), ('@value', (), 2)]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_BoundedCounter_case_02(self):
        self.check(work.BoundedCounter, (0,), ObjectChecks([('increment', (), ValueError)]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_BoundedCounter_case_03(self):
        self.check(work.BoundedCounter, (-1,), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_Cart_case_01(self):
        self.check(work.Cart, (), ObjectChecks([('add', ('a', 3), None), ('add', ('b', 2), None), ('@total', (), 5), ('remove', ('a',), 3), ('@total', (), 2)]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_Cart_case_02(self):
        self.check(work.Cart, (), ObjectChecks([('add', ('x', 4), None), ('add', ('x', -1), ValueError), ('@total', (), 4)]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_Cart_case_03(self):
        self.check(work.Cart, (), ObjectChecks([('remove', ('x',), KeyError), ('@total', (), 0)]),
                   mode=None, dataclass_required=False,
                   frozen=False)
