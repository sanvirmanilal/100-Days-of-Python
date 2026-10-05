"""Behavioral checks for day 034; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_034_generators import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_evens_case_01(self):
        self.check(work.evens, (5,), [0, 2, 4],
                   mode='iterator', dataclass_required=False,
                   frozen=False)

    def test_01_evens_case_02(self):
        self.check(work.evens, (0,), [],
                   mode='iterator', dataclass_required=False,
                   frozen=False)

    def test_01_evens_case_03(self):
        self.check(work.evens, (2,), [0],
                   mode='iterator', dataclass_required=False,
                   frozen=False)

    def test_02_chunks_case_01(self):
        self.check(work.chunks, ([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]],
                   mode='iterator', dataclass_required=False,
                   frozen=False)

    def test_02_chunks_case_02(self):
        self.check(work.chunks, ([], 3), [],
                   mode='iterator', dataclass_required=False,
                   frozen=False)

    def test_02_chunks_case_03(self):
        self.check(work.chunks, ([1], 0), ValueError,
                   mode='iterator', dataclass_required=False,
                   frozen=False)

    def test_03_unique_everseen_case_01(self):
        self.check(work.unique_everseen, (['b', 'a', 'b', 'c'],), ['b', 'a', 'c'],
                   mode='iterator', dataclass_required=False,
                   frozen=False)

    def test_03_unique_everseen_case_02(self):
        self.check(work.unique_everseen, ([],), [],
                   mode='iterator', dataclass_required=False,
                   frozen=False)

    def test_03_unique_everseen_case_03(self):
        self.check(work.unique_everseen, ([0, 0, 1],), [0, 1],
                   mode='iterator', dataclass_required=False,
                   frozen=False)
