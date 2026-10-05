"""Behavioral checks for day 065; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_065_logging import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_parse_log_case_01(self):
        self.check(work.parse_log, ('INFO|ready',), {'level': 'INFO', 'message': 'ready'},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_parse_log_case_02(self):
        self.check(work.parse_log, ('ERROR|a|b',), {'level': 'ERROR', 'message': 'a|b'},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_parse_log_case_03(self):
        self.check(work.parse_log, ('oops',), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_filter_logs_case_01(self):
        self.check(work.filter_logs, ([{'level': 'INFO'}, {'level': 'ERROR'}], 'WARNING'), [{'level': 'ERROR'}],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_filter_logs_case_02(self):
        self.check(work.filter_logs, ([], 'DEBUG'), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_filter_logs_case_03(self):
        self.check(work.filter_logs, ([], 'BAD'), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_error_summary_case_01(self):
        self.check(work.error_summary, (['ERROR|oops', 'INFO|ok', 'ERROR|oops', 'bad'],), {'oops': 2},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_error_summary_case_02(self):
        self.check(work.error_summary, ([],), {},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_error_summary_case_03(self):
        self.check(work.error_summary, (['WARNING|x'],), {},
                   mode=None, dataclass_required=False,
                   frozen=False)
