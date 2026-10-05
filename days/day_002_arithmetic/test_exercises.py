"""Behavioral checks for day 002; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_002_arithmetic import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_minutes_to_seconds_case_01(self):
        self.check(work.minutes_to_seconds, (0,), 0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_minutes_to_seconds_case_02(self):
        self.check(work.minutes_to_seconds, (3,), 180,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_minutes_to_seconds_case_03(self):
        self.check(work.minutes_to_seconds, (125,), 7500,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_rectangle_area_case_01(self):
        self.check(work.rectangle_area, (3, 4), 12,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_rectangle_area_case_02(self):
        self.check(work.rectangle_area, (0, 9), 0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_rectangle_area_case_03(self):
        self.check(work.rectangle_area, (2.5, 4), 10.0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_split_seconds_case_01(self):
        self.check(work.split_seconds, (0,), (0, 0, 0),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_split_seconds_case_02(self):
        self.check(work.split_seconds, (3661,), (1, 1, 1),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_split_seconds_case_03(self):
        self.check(work.split_seconds, (90061,), (25, 1, 1),
                   mode=None, dataclass_required=False,
                   frozen=False)
