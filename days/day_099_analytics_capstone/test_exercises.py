"""Behavioral checks for day 099; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_099_analytics_capstone import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_normalize_transaction_case_01(self):
        self.check(work.normalize_transaction, ({'id': 'a', 'category': 'food', 'cents': -2, 'x': 1},), {'id': 'a', 'category': 'food', 'cents': -2},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_normalize_transaction_case_02(self):
        self.check(work.normalize_transaction, ({'id': '', 'category': 'x', 'cents': 0},), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_normalize_transaction_case_03(self):
        self.check(work.normalize_transaction, ({'id': 'a', 'category': 'x', 'cents': True},), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_clean_transactions_case_01(self):
        self.check(work.clean_transactions, ([{'id': 'a', 'category': 'x', 'cents': 1}, {}, {'id': 'a', 'category': 'y', 'cents': 2}],), [{'id': 'a', 'category': 'x', 'cents': 1}],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_clean_transactions_case_02(self):
        self.check(work.clean_transactions, ([],), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_clean_transactions_case_03(self):
        self.check(work.clean_transactions, ([{'id': 'a', 'category': '', 'cents': 1}, {'id': 'a', 'category': 'x', 'cents': 2}],), [{'id': 'a', 'category': 'x', 'cents': 2}],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_analytics_report_case_01(self):
        self.check(work.analytics_report, ([{'id': 'a', 'category': 'x', 'cents': 3}, {'id': 'b', 'category': 'x', 'cents': -3}, {'id': 'c', 'category': 'y', 'cents': 2}],), {'count': 3, 'total': 2, 'by_category': [('y', 2), ('x', 0)]},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_analytics_report_case_02(self):
        self.check(work.analytics_report, ([],), {'count': 0, 'total': 0, 'by_category': []},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_analytics_report_case_03(self):
        self.check(work.analytics_report, ([{}],), {'count': 0, 'total': 0, 'by_category': []},
                   mode=None, dataclass_required=False,
                   frozen=False)
