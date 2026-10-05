"""Behavioral checks for day 027; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_027_csv import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_parse_csv_case_01(self):
        self.check(work.parse_csv, ('a,b\n1,2\n',), [['a', 'b'], ['1', '2']],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_parse_csv_case_02(self):
        self.check(work.parse_csv, ('',), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_parse_csv_case_03(self):
        self.check(work.parse_csv, ('"a,b",c\n',), [['a,b', 'c']],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_csv_records_case_01(self):
        self.check(work.csv_records, ('name,age\nAda,36\n',), [{'name': 'Ada', 'age': '36'}],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_csv_records_case_02(self):
        self.check(work.csv_records, ('',), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_csv_records_case_03(self):
        self.check(work.csv_records, ('x\n"a,b"\n',), [{'x': 'a,b'}],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_sum_csv_column_case_01(self):
        self.check(work.sum_csv_column, ('x,y\n2,9\n3,8\n', 'x'), 5,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_sum_csv_column_case_02(self):
        self.check(work.sum_csv_column, ('x\n', 'x'), 0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_sum_csv_column_case_03(self):
        self.check(work.sum_csv_column, ('x\n1\n', 'z'), KeyError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_sum_csv_column_case_04(self):
        self.check(work.sum_csv_column, ('x\nno\n', 'x'), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)
