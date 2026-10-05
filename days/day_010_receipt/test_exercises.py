"""Behavioral checks for day 010; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_010_receipt import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_line_total_case_01(self):
        self.check(work.line_total, (250, 3), 750,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_line_total_case_02(self):
        self.check(work.line_total, (0, 5), 0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_line_total_case_03(self):
        self.check(work.line_total, (2, -1), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_subtotal_case_01(self):
        self.check(work.subtotal, ([(100, 2), (250, 1)],), 450,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_subtotal_case_02(self):
        self.check(work.subtotal, ([],), 0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_subtotal_case_03(self):
        self.check(work.subtotal, ([(5, -1)],), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_receipt_case_01(self):
        self.check(work.receipt, ([(100, 2)], 50), {'subtotal': 200, 'discount': 50, 'total': 150},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_receipt_case_02(self):
        self.check(work.receipt, ([], 10), {'subtotal': 0, 'discount': 0, 'total': 0},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_receipt_case_03(self):
        self.check(work.receipt, ([(10, 1)], 20), {'subtotal': 10, 'discount': 10, 'total': 0},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_receipt_case_04(self):
        self.check(work.receipt, ([], -1), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)
