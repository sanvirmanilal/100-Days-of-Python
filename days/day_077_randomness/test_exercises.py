"""Behavioral checks for day 077; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_077_randomness import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_roll_dice_case_01(self):
        self.check(work.roll_dice, (7, 3), [3, 2, 4],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_roll_dice_case_02(self):
        self.check(work.roll_dice, (1, 0), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_roll_dice_case_03(self):
        self.check(work.roll_dice, (1, 3), [2, 5, 1],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_shuffled_case_01(self):
        self.check(work.shuffled, ([1, 2, 3, 4], 0), [3, 1, 2, 4],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_shuffled_case_02(self):
        self.check(work.shuffled, ([], 7), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_shuffled_case_03(self):
        self.check(work.shuffled, (['x'], 1), ['x'],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_dice_histogram_case_01(self):
        self.check(work.dice_histogram, (7, 3), {1: 0, 2: 1, 3: 1, 4: 1, 5: 0, 6: 0},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_dice_histogram_case_02(self):
        self.check(work.dice_histogram, (0, 0), {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_dice_histogram_case_03(self):
        self.check(work.dice_histogram, (1, 3), {1: 1, 2: 1, 3: 0, 4: 0, 5: 1, 6: 0},
                   mode=None, dataclass_required=False,
                   frozen=False)
