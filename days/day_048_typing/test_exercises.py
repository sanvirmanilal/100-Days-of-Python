"""Behavioral checks for day 048; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_048_typing import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_first_present_case_01(self):
        self.check(work.first_present, ([None, 0, 2],), 0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_first_present_case_02(self):
        self.check(work.first_present, ([],), None,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_first_present_case_03(self):
        self.check(work.first_present, ([None, False],), False,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_parse_optional_int_case_01(self):
        self.check(work.parse_optional_int, (' ',), None,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_parse_optional_int_case_02(self):
        self.check(work.parse_optional_int, ('0',), 0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_parse_optional_int_case_03(self):
        self.check(work.parse_optional_int, ('bad',), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_partition_optional_case_01(self):
        self.check(work.partition_optional, ([None, 0, False, None],), ([0, False], 2),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_partition_optional_case_02(self):
        self.check(work.partition_optional, ([],), ([], 0),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_partition_optional_case_03(self):
        self.check(work.partition_optional, (['x'],), (['x'], 0),
                   mode=None, dataclass_required=False,
                   frozen=False)
