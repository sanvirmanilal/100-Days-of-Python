"""Behavioral checks for day 094; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_094_transactions import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_transfer_case_01(self):
        self.check(work.transfer, ({'a': 5, 'b': 1}, 'a', 'b', 3), {'a': 2, 'b': 4},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_transfer_case_02(self):
        self.check(work.transfer, ({'a': 5}, 'a', 'a', 2), {'a': 5},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_transfer_case_03(self):
        self.check(work.transfer, ({'a': 1, 'b': 0}, 'a', 'b', 2), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_batch_transfers_case_01(self):
        self.check(work.batch_transfers, ({'a': 5, 'b': 0}, [('a', 'b', 3), ('b', 'a', 1)]), {'a': 3, 'b': 2},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_batch_transfers_case_02(self):
        self.check(work.batch_transfers, ({}, []), {},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_batch_transfers_case_03(self):
        self.check(work.batch_transfers, ({'a': 5, 'b': 0}, [('a', 'b', 3), ('a', 'b', 3)]), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_reserve_order_case_01(self):
        self.check(work.reserve_order, ({'a': 3, 'b': 2}, {'a': 2, 'b': 1}), {'a': 1, 'b': 1},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_reserve_order_case_02(self):
        self.check(work.reserve_order, ({}, {}), {},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_reserve_order_case_03(self):
        self.check(work.reserve_order, ({'a': 1}, {'a': 2}), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_reserve_order_case_04(self):
        self.check(work.reserve_order, ({}, {'x': 1}), KeyError,
                   mode=None, dataclass_required=False,
                   frozen=False)
