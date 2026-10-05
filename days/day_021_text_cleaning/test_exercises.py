"""Behavioral checks for day 021; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_021_text_cleaning import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_collapse_spaces_case_01(self):
        self.check(work.collapse_spaces, (' a\t b\n',), 'a b',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_collapse_spaces_case_02(self):
        self.check(work.collapse_spaces, ('',), '',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_collapse_spaces_case_03(self):
        self.check(work.collapse_spaces, ('hello!',), 'hello!',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_slugify_case_01(self):
        self.check(work.slugify, (' Hello World ',), 'hello-world',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_slugify_case_02(self):
        self.check(work.slugify, ('',), '',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_slugify_case_03(self):
        self.check(work.slugify, ('A & B',), 'a-&-b',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_word_counts_case_01(self):
        self.check(work.word_counts, ('Hi, hi! Bye.',), {'hi': 2, 'bye': 1},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_word_counts_case_02(self):
        self.check(work.word_counts, ('!?',), {},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_word_counts_case_03(self):
        self.check(work.word_counts, ("It's PYTHON",), {"it's": 1, 'python': 1},
                   mode=None, dataclass_required=False,
                   frozen=False)
