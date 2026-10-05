"""Behavioral checks for day 090; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_090_inventory import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_apply_stock_case_01(self):
        self.check(work.apply_stock, ({'a': 2}, 'a', -1), {'a': 1},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_apply_stock_case_02(self):
        self.check(work.apply_stock, ({}, 'x', 0), {'x': 0},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_apply_stock_case_03(self):
        self.check(work.apply_stock, ({}, 'x', -1), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_replay_stock_case_01(self):
        self.check(work.replay_stock, ([{'sku': 'a', 'delta': 3}, {'sku': 'a', 'delta': -2}],), {'a': 1},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_replay_stock_case_02(self):
        self.check(work.replay_stock, ([],), {},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_replay_stock_case_03(self):
        self.check(work.replay_stock, ([{'sku': 'a', 'delta': -1}, {'sku': 'a', 'delta': 2}],), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_inventory_report_case_01(self):
        self.check(work.inventory_report, ([{'sku': 'a', 'delta': 2}], {'a': 3, 'b': 1}), {'stock': {'a': 2}, 'low_stock': ['a', 'b']},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_inventory_report_case_02(self):
        self.check(work.inventory_report, ([], {}), {'stock': {}, 'low_stock': []},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_inventory_report_case_03(self):
        self.check(work.inventory_report, ([{'sku': 'x', 'delta': -1}], {}), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)
