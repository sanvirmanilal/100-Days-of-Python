"""Behavioral checks for day 015; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_015_parameters import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_repeat_case_01(self):
        self.check(work.repeat, ('ha',), 'haha',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_repeat_case_02(self):
        self.check(work.repeat, ('x', 0), '',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_repeat_case_03(self):
        self.check(work.repeat, ('x', -1), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_join_words_case_01(self):
        self.check(work.join_words, (['a', 'b'],), 'a b',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_join_words_case_02(self):
        self.check(work.join_words, ([], ','), '',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_join_words_case_03(self):
        self.check(work.join_words, (['a', 'b'], '-'), 'a-b',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_add_item_case_01(self):
        self.check(work.add_item, ('a',), ['a'],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_add_item_case_02(self):
        self.check(work.add_item, (3, [1, 2]), [1, 2, 3],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_add_item_case_03(self):
        self.check(work.add_item, (None, []), [None],
                   mode=None, dataclass_required=False,
                   frozen=False)
