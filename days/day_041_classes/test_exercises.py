"""Behavioral checks for day 041; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_041_classes import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_Counter_case_01(self):
        self.check(work.Counter, (), ObjectChecks([('@value', (), 0), ('increment', (), 1), ('increment', (), 2), ('reset', (), None), ('@value', (), 0)]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_Counter_case_02(self):
        self.check(work.Counter, (5,), ObjectChecks([('increment', (), 6), ('reset', (), None), ('@value', (), 5)]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_Counter_case_03(self):
        self.check(work.Counter, (-1,), ObjectChecks([('increment', (), 0)]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_Rectangle_case_01(self):
        self.check(work.Rectangle, (3, 4), ObjectChecks([('area', (), 12), ('perimeter', (), 14)]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_Rectangle_case_02(self):
        self.check(work.Rectangle, (0, 2), ObjectChecks([('area', (), 0), ('perimeter', (), 4)]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_Rectangle_case_03(self):
        self.check(work.Rectangle, (-1, 2), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_BankAccount_case_01(self):
        self.check(work.BankAccount, (10,), ObjectChecks([('deposit', (5,), 15), ('withdraw', (8,), 7), ('withdraw', (8,), ValueError), ('@balance', (), 7)]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_BankAccount_case_02(self):
        self.check(work.BankAccount, (), ObjectChecks([('deposit', (-1,), ValueError), ('@balance', (), 0)]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_BankAccount_case_03(self):
        self.check(work.BankAccount, (-1,), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)
