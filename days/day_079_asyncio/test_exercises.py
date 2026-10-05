"""Behavioral checks for day 079; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_079_asyncio import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_async_double_case_01(self):
        self.check(work.async_double, (3,), 6,
                   mode='async', dataclass_required=False,
                   frozen=False)

    def test_01_async_double_case_02(self):
        self.check(work.async_double, (0,), 0,
                   mode='async', dataclass_required=False,
                   frozen=False)

    def test_01_async_double_case_03(self):
        self.check(work.async_double, (-2,), -4,
                   mode='async', dataclass_required=False,
                   frozen=False)

    def test_02_gather_values_case_01(self):
        self.check(work.gather_values, ([3, 1, 2],), [3, 1, 2],
                   mode='async', dataclass_required=False,
                   frozen=False)

    def test_02_gather_values_case_02(self):
        self.check(work.gather_values, ([],), [],
                   mode='async', dataclass_required=False,
                   frozen=False)

    def test_02_gather_values_case_03(self):
        self.check(work.gather_values, ([None, False],), [None, False],
                   mode='async', dataclass_required=False,
                   frozen=False)

    def test_03_async_apply_case_01(self):
        self.check(work.async_apply, ('CALL:abs', [-2, 3]), [2, 3],
                   mode='async', dataclass_required=False,
                   frozen=False)

    def test_03_async_apply_case_02(self):
        self.check(work.async_apply, ('CALL:str', []), [],
                   mode='async', dataclass_required=False,
                   frozen=False)

    def test_03_async_apply_case_03(self):
        self.check(work.async_apply, ('CALL:int', ['bad']), ValueError,
                   mode='async', dataclass_required=False,
                   frozen=False)
