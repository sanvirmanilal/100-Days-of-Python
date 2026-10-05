"""Behavioral checks for day 036; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_036_higher_order import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_apply_all_case_01(self):
        self.check(work.apply_all, ('CALL:int', ['1', '2']), [1, 2],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_apply_all_case_02(self):
        self.check(work.apply_all, ('CALL:str', []), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_apply_all_case_03(self):
        self.check(work.apply_all, ('CALL:abs', [-2, 3]), [2, 3],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_filter_by_case_01(self):
        self.check(work.filter_by, ('CALL:bool', [0, 1, '', 2]), [1, 2],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_filter_by_case_02(self):
        self.check(work.filter_by, ('CALL:bool', []), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_filter_by_case_03(self):
        self.check(work.filter_by, ('CALL:str.isupper', ['A', 'a', 'B']), ['A', 'B'],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_compose_apply_case_01(self):
        self.check(work.compose_apply, (['CALL:str.upper', 'CALL:str.strip'], ' hi '), 'HI',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_compose_apply_case_02(self):
        self.check(work.compose_apply, ([], 3), 3,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_compose_apply_case_03(self):
        self.check(work.compose_apply, (['CALL:abs', 'CALL:int'], '-7'), 7,
                   mode=None, dataclass_required=False,
                   frozen=False)
