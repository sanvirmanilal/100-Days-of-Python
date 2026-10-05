"""Behavioral checks for day 020; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_020_leaderboard import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_total_points_case_01(self):
        self.check(work.total_points, ([('a', 2), ('b', 1), ('a', 3)],), {'a': 5, 'b': 1},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_total_points_case_02(self):
        self.check(work.total_points, ([],), {},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_total_points_case_03(self):
        self.check(work.total_points, ([('a', -1), ('a', 1)],), {'a': 0},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_top_players_case_01(self):
        self.check(work.top_players, ({'b': 4, 'a': 4, 'c': 2}, 2), [('a', 4), ('b', 4)],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_top_players_case_02(self):
        self.check(work.top_players, ({}, 3), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_top_players_case_03(self):
        self.check(work.top_players, ({'x': 2}, 0), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_top_players_case_04(self):
        self.check(work.top_players, ({}, -1), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_competition_ranks_case_01(self):
        self.check(work.competition_ranks, ({'b': 5, 'a': 5, 'c': 3},), [('a', 5, 1), ('b', 5, 1), ('c', 3, 3)],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_competition_ranks_case_02(self):
        self.check(work.competition_ranks, ({},), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_competition_ranks_case_03(self):
        self.check(work.competition_ranks, ({'x': 9},), [('x', 9, 1)],
                   mode=None, dataclass_required=False,
                   frozen=False)
