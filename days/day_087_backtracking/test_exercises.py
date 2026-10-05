"""Behavioral checks for day 087; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_087_backtracking import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_subsets_case_01(self):
        self.check(work.subsets, (['a', 'b'],), [[], ['a'], ['b'], ['a', 'b']],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_subsets_case_02(self):
        self.check(work.subsets, ([],), [[]],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_subsets_case_03(self):
        self.check(work.subsets, ([1],), [[], [1]],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_balanced_parentheses_case_01(self):
        self.check(work.balanced_parentheses, (2,), ['(())', '()()'],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_balanced_parentheses_case_02(self):
        self.check(work.balanced_parentheses, (0,), [''],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_balanced_parentheses_case_03(self):
        self.check(work.balanced_parentheses, (3,), ['((()))', '(()())', '(())()', '()(())', '()()()'],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_n_queens_count_case_01(self):
        self.check(work.n_queens_count, (0,), 1,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_n_queens_count_case_02(self):
        self.check(work.n_queens_count, (4,), 2,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_n_queens_count_case_03(self):
        self.check(work.n_queens_count, (5,), 10,
                   mode=None, dataclass_required=False,
                   frozen=False)
