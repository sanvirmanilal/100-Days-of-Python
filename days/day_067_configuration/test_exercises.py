"""Behavioral checks for day 067; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_067_configuration import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_merge_config_case_01(self):
        self.check(work.merge_config, ({'x': 1}, {'x': 2}, {'y': 3}), {'x': 2, 'y': 3},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_merge_config_case_02(self):
        self.check(work.merge_config, ({}, {}, {}), {},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_merge_config_case_03(self):
        self.check(work.merge_config, ({'x': 1}, {}, {'x': None}), {'x': None},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_parse_bool_case_01(self):
        self.check(work.parse_bool, (' YES ',), True,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_parse_bool_case_02(self):
        self.check(work.parse_bool, ('0',), False,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_parse_bool_case_03(self):
        self.check(work.parse_bool, ('maybe',), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_validate_config_case_01(self):
        self.check(work.validate_config, ({'host': 'localhost', 'port': 8080, 'x': 1},), {'host': 'localhost', 'port': 8080},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_validate_config_case_02(self):
        self.check(work.validate_config, ({'host': '', 'port': 1},), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_validate_config_case_03(self):
        self.check(work.validate_config, ({'host': 'x', 'port': True},), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_validate_config_case_04(self):
        self.check(work.validate_config, ({},), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)
