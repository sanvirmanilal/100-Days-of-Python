"""Behavioral checks for day 046; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_046_context_managers import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_read_first_line_case_01(self):
        self.check(work.read_first_line, (File(' hi \nnext'),), ' hi ',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_read_first_line_case_02(self):
        self.check(work.read_first_line, (File(''),), '',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_read_first_line_case_03(self):
        self.check(work.read_first_line, (File('one'),), 'one',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_capture_output_case_01(self):
        self.check(work.capture_output, ('CALL:print_ready',), 'ready\n',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_capture_output_case_02(self):
        self.check(work.capture_output, ('CALL:print_nothing',), '',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_capture_output_case_03(self):
        self.check(work.capture_output, ('CALL:raise_value',), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_temporary_setting_case_01(self):
        self.check(work.temporary_setting, ({'x': 1}, 'x', 9, 'CALL:read_x'), 9,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_temporary_setting_case_02(self):
        self.check(work.temporary_setting, ({}, 'x', 3, 'CALL:read_x'), 3,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_temporary_setting_case_03(self):
        self.check(work.temporary_setting, ({'x': 2}, 'x', 8, 'CALL:raise_value'), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)
