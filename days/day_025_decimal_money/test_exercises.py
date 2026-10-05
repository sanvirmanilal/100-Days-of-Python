"""Behavioral checks for day 025; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_025_decimal_money import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_money_case_01(self):
        self.check(work.money, ('1.005',), '1.01',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_money_case_02(self):
        self.check(work.money, ('2',), '2.00',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_money_case_03(self):
        self.check(work.money, ('-1.005',), '-1.01',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_add_money_case_01(self):
        self.check(work.add_money, (['0.1', '0.2'],), '0.30',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_add_money_case_02(self):
        self.check(work.add_money, ([],), '0.00',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_add_money_case_03(self):
        self.check(work.add_money, (['0.005', '0.005'],), '0.01',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_allocate_cents_case_01(self):
        self.check(work.allocate_cents, (10, 3), [4, 3, 3],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_allocate_cents_case_02(self):
        self.check(work.allocate_cents, (0, 2), [0, 0],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_allocate_cents_case_03(self):
        self.check(work.allocate_cents, (1, 0), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_allocate_cents_case_04(self):
        self.check(work.allocate_cents, (-1, 2), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)
