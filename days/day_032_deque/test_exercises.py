"""Behavioral checks for day 032; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_032_deque import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_serve_queue_case_01(self):
        self.check(work.serve_queue, (['a', 'b'],), ['a', 'b'],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_serve_queue_case_02(self):
        self.check(work.serve_queue, ([],), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_serve_queue_case_03(self):
        self.check(work.serve_queue, (['a', 'a'],), ['a', 'a'],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_recent_items_case_01(self):
        self.check(work.recent_items, ([1, 2, 3], 2), [2, 3],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_recent_items_case_02(self):
        self.check(work.recent_items, ([1], 0), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_recent_items_case_03(self):
        self.check(work.recent_items, ([], 3), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_round_robin_case_01(self):
        self.check(work.round_robin, ([[1, 2], ['a'], [True, False]],), [1, 'a', True, 2, False],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_round_robin_case_02(self):
        self.check(work.round_robin, ([[], [1, 2]],), [1, 2],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_round_robin_case_03(self):
        self.check(work.round_robin, ([],), [],
                   mode=None, dataclass_required=False,
                   frozen=False)
