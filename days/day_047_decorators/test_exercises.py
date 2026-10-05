"""Behavioral checks for day 047; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_047_decorators import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_call_repeated_case_01(self):
        self.check(work.call_repeated, ('CALL:abs', 3, (-2,)), [2, 2, 2],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_call_repeated_case_02(self):
        self.check(work.call_repeated, ('CALL:int', 0, ('1',)), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_call_repeated_case_03(self):
        self.check(work.call_repeated, ('CALL:str', 1, (5,)), ['5'],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_Counted_case_01(self):
        self.check(work.Counted, ('CALL:abs',), ObjectChecks([('__call__', (-2,), 2), ('__call__', (3,), 3), ('@calls', (), 2)]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_Counted_case_02(self):
        self.check(work.Counted, ('CALL:int',), ObjectChecks([('__call__', ('bad',), ValueError), ('@calls', (), 1)]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_Counted_case_03(self):
        self.check(work.Counted, ('CALL:str',), ObjectChecks([('@calls', (), 0)]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_Memoized_case_01(self):
        self.check(work.Memoized, ('CALL:abs',), ObjectChecks([('__call__', (-2,), 2), ('__call__', (-2,), 2), ('@cache', (), {(-2,): 2})]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_Memoized_case_02(self):
        self.check(work.Memoized, ('CALL:int',), ObjectChecks([('__call__', ('bad',), ValueError), ('@cache', (), {})]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_Memoized_case_03(self):
        self.check(work.Memoized, ('CALL:str',), ObjectChecks([('__call__', (1,), '1'), ('__call__', (2,), '2'), ('@cache', (), {(1,): '1', (2,): '2'})]),
                   mode=None, dataclass_required=False,
                   frozen=False)
