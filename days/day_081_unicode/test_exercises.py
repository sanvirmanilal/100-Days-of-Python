"""Behavioral checks for day 081; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_081_unicode import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_utf8_length_case_01(self):
        self.check(work.utf8_length, ('abc',), 3,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_utf8_length_case_02(self):
        self.check(work.utf8_length, ('é',), 2,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_utf8_length_case_03(self):
        self.check(work.utf8_length, ('',), 0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_normalized_equal_case_01(self):
        self.check(work.normalized_equal, ('é', 'é'), True,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_normalized_equal_case_02(self):
        self.check(work.normalized_equal, ('Straße', 'STRASSE'), True,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_normalized_equal_case_03(self):
        self.check(work.normalized_equal, ('a', 'b'), False,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_unique_normalized_case_01(self):
        self.check(work.unique_normalized, (['É', 'é', 'Straße', 'STRASSE'],), ['é', 'strasse'],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_unique_normalized_case_02(self):
        self.check(work.unique_normalized, ([],), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_unique_normalized_case_03(self):
        self.check(work.unique_normalized, (['A', 'a', 'B'],), ['a', 'b'],
                   mode=None, dataclass_required=False,
                   frozen=False)
