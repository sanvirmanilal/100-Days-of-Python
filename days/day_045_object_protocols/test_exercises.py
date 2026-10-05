"""Behavioral checks for day 045; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_045_object_protocols import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_Playlist_case_01(self):
        self.check(work.Playlist, (['a', 'b'],), ObjectChecks([('__len__', (), 2), ('__contains__', ('a',), True), ('__contains__', ('x',), False), ('!list', (), ['a', 'b'])]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_Playlist_case_02(self):
        self.check(work.Playlist, ([],), ObjectChecks([('__len__', (), 0), ('!list', (), [])]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_Playlist_case_03(self):
        self.check(work.Playlist, (['a', 'a'],), ObjectChecks([('!list', (), ['a', 'a'])]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_RangeBox_case_01(self):
        self.check(work.RangeBox, (2, 4), ObjectChecks([('__contains__', (3,), True), ('__contains__', (5,), False), ('__len__', (), 3)]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_RangeBox_case_02(self):
        self.check(work.RangeBox, (0, 0), ObjectChecks([('__len__', (), 1)]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_RangeBox_case_03(self):
        self.check(work.RangeBox, (3, 2), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_Polynomial_case_01(self):
        self.check(work.Polynomial, ([1, 2, 3],), ObjectChecks([('__call__', (2,), 17), ('__len__', (), 3)]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_Polynomial_case_02(self):
        self.check(work.Polynomial, ([],), ObjectChecks([('__call__', (8,), 0), ('__len__', (), 0)]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_Polynomial_case_03(self):
        self.check(work.Polynomial, ([0, 1],), ObjectChecks([('__call__', (-3,), -3)]),
                   mode=None, dataclass_required=False,
                   frozen=False)
