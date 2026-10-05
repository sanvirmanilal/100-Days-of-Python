"""Behavioral checks for day 051; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_051_stacks import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_reverse_with_stack_case_01(self):
        self.check(work.reverse_with_stack, ([1, 2, 3],), [3, 2, 1],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_reverse_with_stack_case_02(self):
        self.check(work.reverse_with_stack, ([],), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_reverse_with_stack_case_03(self):
        self.check(work.reverse_with_stack, (['x'],), ['x'],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_balanced_case_01(self):
        self.check(work.balanced, ('a([]){}',), True,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_balanced_case_02(self):
        self.check(work.balanced, ('([)]',), False,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_balanced_case_03(self):
        self.check(work.balanced, ('',), True,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_balanced_case_04(self):
        self.check(work.balanced, ('(',), False,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_evaluate_rpn_case_01(self):
        self.check(work.evaluate_rpn, (['2', '3', '+', '4', '*'],), 20,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_evaluate_rpn_case_02(self):
        self.check(work.evaluate_rpn, (['5', '2', '-'],), 3,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_evaluate_rpn_case_03(self):
        self.check(work.evaluate_rpn, (['1', '2'],), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_evaluate_rpn_case_04(self):
        self.check(work.evaluate_rpn, (['+'],), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)
