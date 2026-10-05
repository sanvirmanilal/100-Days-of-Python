"""Behavioral checks for day 011; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_011_slicing import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_first_last_case_01(self):
        self.check(work.first_last, ([1, 2, 3],), (1, 3),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_first_last_case_02(self):
        self.check(work.first_last, ([4],), (4, 4),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_first_last_case_03(self):
        self.check(work.first_last, ([],), None,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_every_other_case_01(self):
        self.check(work.every_other, ([1, 2, 3, 4, 5],), [1, 3, 5],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_every_other_case_02(self):
        self.check(work.every_other, ([],), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_every_other_case_03(self):
        self.check(work.every_other, ([7],), [7],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_rotate_case_01(self):
        self.check(work.rotate, ([1, 2, 3], 1), [3, 1, 2],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_rotate_case_02(self):
        self.check(work.rotate, ([1, 2, 3], -1), [2, 3, 1],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_rotate_case_03(self):
        self.check(work.rotate, ([], 100), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_rotate_case_04(self):
        self.check(work.rotate, ([1, 2, 3], 7), [3, 1, 2],
                   mode=None, dataclass_required=False,
                   frozen=False)
