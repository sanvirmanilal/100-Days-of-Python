"""Behavioral checks for day 019; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_019_sorting import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_sort_numbers_case_01(self):
        self.check(work.sort_numbers, ([3, 1, 2],), [1, 2, 3],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_sort_numbers_case_02(self):
        self.check(work.sort_numbers, ([],), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_sort_numbers_case_03(self):
        self.check(work.sort_numbers, ([-1, 2, -1],), [-1, -1, 2],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_sort_words_case_01(self):
        self.check(work.sort_words, (['bb', 'a', 'aa'],), ['a', 'aa', 'bb'],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_sort_words_case_02(self):
        self.check(work.sort_words, ([],), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_sort_words_case_03(self):
        self.check(work.sort_words, (['b', 'A', 'a'],), ['A', 'a', 'b'],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_rank_players_case_01(self):
        self.check(work.rank_players, ([{'name': 'Bo', 'score': 5}, {'name': 'Ada', 'score': 5}, {'name': 'Cy', 'score': 9}],), [{'name': 'Cy', 'score': 9}, {'name': 'Ada', 'score': 5}, {'name': 'Bo', 'score': 5}],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_rank_players_case_02(self):
        self.check(work.rank_players, ([],), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_rank_players_case_03(self):
        self.check(work.rank_players, ([{'name': 'X', 'score': 0}],), [{'name': 'X', 'score': 0}],
                   mode=None, dataclass_required=False,
                   frozen=False)
