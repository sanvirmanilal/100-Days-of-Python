"""Behavioral checks for day 078; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_078_futures import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_parallel_map_case_01(self):
        self.check(work.parallel_map, ('CALL:abs', [-2, 3]), [2, 3],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_parallel_map_case_02(self):
        self.check(work.parallel_map, ('CALL:str', []), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_parallel_map_case_03(self):
        self.check(work.parallel_map, ('CALL:int', ['bad']), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_parallel_lengths_case_01(self):
        self.check(work.parallel_lengths, (['abc', 'x'],), [('abc', 3), ('x', 1)],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_parallel_lengths_case_02(self):
        self.check(work.parallel_lengths, ([],), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_parallel_lengths_case_03(self):
        self.check(work.parallel_lengths, (['', 'é'],), [('', 0), ('é', 1)],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_parallel_batches_case_01(self):
        self.check(work.parallel_batches, ('CALL:abs', [[-1, 2], [], [-3]]), [[1, 2], [], [3]],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_parallel_batches_case_02(self):
        self.check(work.parallel_batches, ('CALL:str', []), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_parallel_batches_case_03(self):
        self.check(work.parallel_batches, ('CALL:int', [['bad']]), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)
