"""Behavioral checks for day 012; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_012_tuples import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_move_case_01(self):
        self.check(work.move, ((1, 2), (3, -1)), (4, 1),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_move_case_02(self):
        self.check(work.move, ((0, 0), (0, 0)), (0, 0),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_move_case_03(self):
        self.check(work.move, ((-1, 4), (1, 2)), (0, 6),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_bounds_case_01(self):
        self.check(work.bounds, ([3, 1, 7],), (1, 7),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_bounds_case_02(self):
        self.check(work.bounds, ([],), None,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_bounds_case_03(self):
        self.check(work.bounds, ([-2, -2],), (-2, -2),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_zip_strict_case_01(self):
        self.check(work.zip_strict, ([1, 2], ['a', 'b']), [(1, 'a'), (2, 'b')],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_zip_strict_case_02(self):
        self.check(work.zip_strict, ([], []), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_zip_strict_case_03(self):
        self.check(work.zip_strict, ([1], []), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)
