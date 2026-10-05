"""Behavioral checks for day 095; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_095_thread_safety import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_SafeCounter_case_01(self):
        self.check(work.SafeCounter, (0,), ObjectChecks([('increment', (), 1), ('increment', (3,), 4), ('@value', (), 4)]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_SafeCounter_case_02(self):
        self.check(work.SafeCounter, (5,), ObjectChecks([('increment', (-2,), 3)]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_SafeCounter_case_03(self):
        self.check(work.SafeCounter, (), ObjectChecks([('@value', (), 0)]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_count_in_threads_case_01(self):
        self.check(work.count_in_threads, (4, 1000), 4000,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_count_in_threads_case_02(self):
        self.check(work.count_in_threads, (0, 10), 0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_count_in_threads_case_03(self):
        self.check(work.count_in_threads, (-1, 2), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_LockedInventory_case_01(self):
        self.check(work.LockedInventory, ({'a': 3},), ObjectChecks([('buy', ('a', 2), 1), ('buy', ('a', 2), ValueError), ('snapshot', (), {'a': 1})]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_LockedInventory_case_02(self):
        self.check(work.LockedInventory, ({},), ObjectChecks([('buy', ('x', 1), KeyError)]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_LockedInventory_case_03(self):
        self.check(work.LockedInventory, ({'a': 1},), ObjectChecks([('buy', ('a', 0), ValueError), ('snapshot', (), {'a': 1})]),
                   mode=None, dataclass_required=False,
                   frozen=False)
