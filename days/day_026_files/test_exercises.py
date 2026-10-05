"""Behavioral checks for day 026; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_026_files import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_read_text_case_01(self):
        self.check(work.read_text, (File('hello\n'),), 'hello\n',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_read_text_case_02(self):
        self.check(work.read_text, (File(''),), '',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_read_text_case_03(self):
        self.check(work.read_text, (File('café'),), 'café',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_nonempty_lines_case_01(self):
        self.check(work.nonempty_lines, (File(' a \n\n b\t\n'),), ['a', 'b'],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_nonempty_lines_case_02(self):
        self.check(work.nonempty_lines, (File(''),), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_nonempty_lines_case_03(self):
        self.check(work.nonempty_lines, (File(' café '),), ['café'],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_file_stats_case_01(self):
        self.check(work.file_stats, (File('a b\nc\n'),), {'lines': 2, 'words': 3, 'characters': 6},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_file_stats_case_02(self):
        self.check(work.file_stats, (File(''),), {'lines': 0, 'words': 0, 'characters': 0},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_file_stats_case_03(self):
        self.check(work.file_stats, (File('é'),), {'lines': 1, 'words': 1, 'characters': 1},
                   mode=None, dataclass_required=False,
                   frozen=False)
