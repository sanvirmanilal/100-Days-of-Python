"""Behavioral checks for day 088; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_088_expression_parser import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_tokenize_case_01(self):
        self.check(work.tokenize, ('12 + (3*4)',), [12, '+', '(', 3, '*', 4, ')'],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_tokenize_case_02(self):
        self.check(work.tokenize, ('',), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_tokenize_case_03(self):
        self.check(work.tokenize, ('1-2',), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_evaluate_flat_case_01(self):
        self.check(work.evaluate_flat, ('1 + 2 + 30',), 33,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_evaluate_flat_case_02(self):
        self.check(work.evaluate_flat, ('0',), 0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_evaluate_flat_case_03(self):
        self.check(work.evaluate_flat, ('1+',), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_evaluate_flat_case_04(self):
        self.check(work.evaluate_flat, ('1 2',), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_evaluate_case_01(self):
        self.check(work.evaluate, ('2+3*4',), 14,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_evaluate_case_02(self):
        self.check(work.evaluate, ('(2+3)*4',), 20,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_evaluate_case_03(self):
        self.check(work.evaluate, ('2**3',), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_evaluate_case_04(self):
        self.check(work.evaluate, ('',), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)
