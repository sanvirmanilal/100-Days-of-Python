"""Behavioral checks for day 089; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_089_events import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_balance_events_case_01(self):
        self.check(work.balance_events, ([('deposit', 5), ('withdraw', 2)],), 3,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_balance_events_case_02(self):
        self.check(work.balance_events, ([],), 0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_balance_events_case_03(self):
        self.check(work.balance_events, ([('withdraw', 1)],), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_replay_counter_case_01(self):
        self.check(work.replay_counter, ([('add', 2), ('set', 7), ('add', -1)],), [0, 2, 7, 6],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_replay_counter_case_02(self):
        self.check(work.replay_counter, ([],), [0],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_replay_counter_case_03(self):
        self.check(work.replay_counter, ([('oops', 1)],), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_deduplicate_events_case_01(self):
        self.check(work.deduplicate_events, ([{'id': 1, 'v': 'a'}, {'id': 1, 'v': 'b'}, {'id': 2, 'v': 'c'}],), [{'id': 1, 'v': 'a'}, {'id': 2, 'v': 'c'}],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_deduplicate_events_case_02(self):
        self.check(work.deduplicate_events, ([],), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_deduplicate_events_case_03(self):
        self.check(work.deduplicate_events, ([{'id': 0}],), [{'id': 0}],
                   mode=None, dataclass_required=False,
                   frozen=False)
