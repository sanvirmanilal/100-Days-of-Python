"""Behavioral checks for day 029; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_029_paths import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_file_extension_case_01(self):
        self.check(work.file_extension, ('a/B.TXT',), '.txt',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_file_extension_case_02(self):
        self.check(work.file_extension, ('README',), '',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_file_extension_case_03(self):
        self.check(work.file_extension, ('archive.tar.gz',), '.gz',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_replace_extension_case_01(self):
        self.check(work.replace_extension, ('a/b.txt', '.csv'), 'a/b.csv',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_replace_extension_case_02(self):
        self.check(work.replace_extension, ('file', ''), 'file',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_replace_extension_case_03(self):
        self.check(work.replace_extension, ('a.tar.gz', '.zip'), 'a.tar.zip',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_safe_relative_case_01(self):
        self.check(work.safe_relative, ('images/a.png',), True,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_safe_relative_case_02(self):
        self.check(work.safe_relative, ('../secret',), False,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_safe_relative_case_03(self):
        self.check(work.safe_relative, ('/etc/passwd',), False,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_safe_relative_case_04(self):
        self.check(work.safe_relative, ('a/../b',), False,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_safe_relative_case_05(self):
        self.check(work.safe_relative, ('',), True,
                   mode=None, dataclass_required=False,
                   frozen=False)
