"""Behavioral checks for day 066; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_066_command_line import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_parse_name_case_01(self):
        self.check(work.parse_name, ([],), 'world',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_parse_name_case_02(self):
        self.check(work.parse_name, (['--name', 'Ada'],), 'Ada',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_parse_name_case_03(self):
        self.check(work.parse_name, (['--unknown'],), SystemExit,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_parse_count_case_01(self):
        self.check(work.parse_count, ([],), 1,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_parse_count_case_02(self):
        self.check(work.parse_count, (['--count', '3'],), 3,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_parse_count_case_03(self):
        self.check(work.parse_count, (['--count', 'x'],), SystemExit,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_parse_cli_case_01(self):
        self.check(work.parse_cli, (['list'],), {'action': 'list', 'limit': 10, 'verbose': False},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_parse_cli_case_02(self):
        self.check(work.parse_cli, (['add', '--limit', '2', '--verbose'],), {'action': 'add', 'limit': 2, 'verbose': True},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_parse_cli_case_03(self):
        self.check(work.parse_cli, (['delete'],), SystemExit,
                   mode=None, dataclass_required=False,
                   frozen=False)
