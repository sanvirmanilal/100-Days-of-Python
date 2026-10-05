"""Behavioral checks for day 030; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_030_expense_report import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_validate_expense_case_01(self):
        self.check(work.validate_expense, ({'category': 'food', 'cents': 0},), True,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_validate_expense_case_02(self):
        self.check(work.validate_expense, ({'category': '', 'cents': 1},), False,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_validate_expense_case_03(self):
        self.check(work.validate_expense, ({'category': 'x', 'cents': True},), False,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_validate_expense_case_04(self):
        self.check(work.validate_expense, ([],), False,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_category_totals_case_01(self):
        self.check(work.category_totals, ([{'category': 'a', 'cents': 2}, {'category': 'a', 'cents': 3}],), {'a': 5},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_category_totals_case_02(self):
        self.check(work.category_totals, ([],), {},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_category_totals_case_03(self):
        self.check(work.category_totals, ([{'category': 'x', 'cents': -1}],), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_expense_report_case_01(self):
        self.check(work.expense_report, ([{'category': 'b', 'cents': 2}, {'category': 'a', 'cents': 2}],), {'total': 4, 'categories': [('a', 2), ('b', 2)]},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_expense_report_case_02(self):
        self.check(work.expense_report, ([],), {'total': 0, 'categories': []},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_expense_report_case_03(self):
        self.check(work.expense_report, ([{'category': 'x', 'cents': -1}],), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)
