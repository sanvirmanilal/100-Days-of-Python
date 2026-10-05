"""Behavioral checks for day 064; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_064_test_doubles import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_notify_all_case_01(self):
        self.check(work.notify_all, (['a', 'b'], 'CALL:noop'), 2,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_notify_all_case_02(self):
        self.check(work.notify_all, ([], 'CALL:noop'), 0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_notify_all_case_03(self):
        self.check(work.notify_all, (['a'], 'CALL:raise_value'), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_Spy_case_01(self):
        self.check(work.Spy, ('CALL:abs',), ObjectChecks([('__call__', (-2,), 2), ('@calls', (), [(-2,)])]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_Spy_case_02(self):
        self.check(work.Spy, ('CALL:int',), ObjectChecks([('__call__', ('bad',), ValueError), ('@calls', (), [('bad',)])]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_Spy_case_03(self):
        self.check(work.Spy, ('CALL:str',), ObjectChecks([('@calls', (), [])]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_fallback_call_case_01(self):
        self.check(work.fallback_call, ('CALL:abs', 'CALL:str', -2), 2,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_fallback_call_case_02(self):
        self.check(work.fallback_call, ('CALL:always_missing', 'CALL:str', 3), '3',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_fallback_call_case_03(self):
        self.check(work.fallback_call, ('CALL:raise_value', 'CALL:str', 3), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)
