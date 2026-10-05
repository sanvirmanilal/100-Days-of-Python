"""Behavioral checks for day 003; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_003_strings import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_shout_case_01(self):
        self.check(work.shout, ('hello',), 'HELLO',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_shout_case_02(self):
        self.check(work.shout, ('',), '',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_shout_case_03(self):
        self.check(work.shout, ('Hi 2!',), 'HI 2!',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_initials_case_01(self):
        self.check(work.initials, ('ada', 'lovelace'), 'A.L.',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_initials_case_02(self):
        self.check(work.initials, (' Bo ', ' chen '), 'B.C.',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_initials_case_03(self):
        self.check(work.initials, ('éva', 'smith'), 'É.S.',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_frame_case_01(self):
        self.check(work.frame, ('Hi', '*'), '******\n* Hi *\n******',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_frame_case_02(self):
        self.check(work.frame, ('', '#'), '####\n#  #\n####',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_frame_case_03(self):
        self.check(work.frame, ('cat', '-'), '-------\n- cat -\n-------',
                   mode=None, dataclass_required=False,
                   frozen=False)
