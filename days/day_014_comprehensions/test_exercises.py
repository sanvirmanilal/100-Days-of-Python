"""Behavioral checks for day 014; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_014_comprehensions import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_squares_case_01(self):
        self.check(work.squares, (4,), [0, 1, 4, 9],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_squares_case_02(self):
        self.check(work.squares, (0,), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_squares_case_03(self):
        self.check(work.squares, (1,), [0],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_length_map_case_01(self):
        self.check(work.length_map, (['a', 'cat', 'a'],), {'a': 1, 'cat': 3},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_length_map_case_02(self):
        self.check(work.length_map, ([],), {},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_length_map_case_03(self):
        self.check(work.length_map, ([''],), {'': 0},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_flatten_case_01(self):
        self.check(work.flatten, ([[1, 2], [], [3]],), [1, 2, 3],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_flatten_case_02(self):
        self.check(work.flatten, ([],), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_flatten_case_03(self):
        self.check(work.flatten, ([[], []],), [],
                   mode=None, dataclass_required=False,
                   frozen=False)
