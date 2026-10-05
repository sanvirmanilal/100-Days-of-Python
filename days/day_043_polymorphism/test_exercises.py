"""Behavioral checks for day 043; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_043_polymorphism import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_FixedDiscount_case_01(self):
        self.check(work.FixedDiscount, (3,), ObjectChecks([('apply', (10,), 7), ('apply', (2,), 0)]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_FixedDiscount_case_02(self):
        self.check(work.FixedDiscount, (0,), ObjectChecks([('apply', (5,), 5)]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_FixedDiscount_case_03(self):
        self.check(work.FixedDiscount, (-1,), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_PercentDiscount_case_01(self):
        self.check(work.PercentDiscount, (25,), ObjectChecks([('apply', (10,), 8), ('apply', (100,), 75)]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_PercentDiscount_case_02(self):
        self.check(work.PercentDiscount, (100,), ObjectChecks([('apply', (5,), 0)]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_PercentDiscount_case_03(self):
        self.check(work.PercentDiscount, (101,), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_discounted_total_case_01(self):
        self.check(work.discounted_total, (10, ['CALL:abs', 'CALL:float']), 10.0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_discounted_total_case_02(self):
        self.check(work.discounted_total, (-3, ['CALL:abs']), 3,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_discounted_total_case_03(self):
        self.check(work.discounted_total, (5, []), 5,
                   mode=None, dataclass_required=False,
                   frozen=False)
