"""Behavioral checks for day 049; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_049_enums import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_traffic_next_case_01(self):
        self.check(work.traffic_next, ('red',), 'green',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_traffic_next_case_02(self):
        self.check(work.traffic_next, ('amber',), 'red',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_traffic_next_case_03(self):
        self.check(work.traffic_next, ('blue',), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_order_transition_case_01(self):
        self.check(work.order_transition, ('new', 'pay'), 'paid',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_order_transition_case_02(self):
        self.check(work.order_transition, ('paid', 'ship'), 'shipped',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_order_transition_case_03(self):
        self.check(work.order_transition, ('shipped', 'cancel'), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_run_order_case_01(self):
        self.check(work.run_order, (['pay', 'ship'],), 'shipped',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_run_order_case_02(self):
        self.check(work.run_order, ([],), 'new',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_run_order_case_03(self):
        self.check(work.run_order, (['cancel', 'pay'],), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)
