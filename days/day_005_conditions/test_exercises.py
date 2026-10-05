"""Behavioral checks for day 005; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_005_conditions import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_sign_case_01(self):
        self.check(work.sign, (5,), 'positive',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_sign_case_02(self):
        self.check(work.sign, (-1,), 'negative',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_sign_case_03(self):
        self.check(work.sign, (0,), 'zero',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_grade_case_01(self):
        self.check(work.grade, (90,), 'A',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_grade_case_02(self):
        self.check(work.grade, (79,), 'C',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_grade_case_03(self):
        self.check(work.grade, (59,), 'F',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_grade_case_04(self):
        self.check(work.grade, (101,), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_grade_case_05(self):
        self.check(work.grade, (-1,), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_shipping_cost_case_01(self):
        self.check(work.shipping_cost, (50, False), 0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_shipping_cost_case_02(self):
        self.check(work.shipping_cost, (49, True), 2,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_shipping_cost_case_03(self):
        self.check(work.shipping_cost, (0, False), 5,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_shipping_cost_case_04(self):
        self.check(work.shipping_cost, (-1, True), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)
