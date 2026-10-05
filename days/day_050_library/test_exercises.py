"""Behavioral checks for day 050; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_050_library import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_Book_case_01(self):
        self.check(work.Book, ('Python', 2), ObjectChecks([('@title', (), 'Python'), ('available', (), 2)]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_Book_case_02(self):
        self.check(work.Book, ('', 1), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_Book_case_03(self):
        self.check(work.Book, ('X', -1), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_LendingDesk_case_01(self):
        self.check(work.LendingDesk, ({'a': 1},), ObjectChecks([('borrow', ('a',), None), ('available', ('a',), 0), ('borrow', ('a',), ValueError)]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_LendingDesk_case_02(self):
        self.check(work.LendingDesk, ({},), ObjectChecks([('borrow', ('x',), KeyError)]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_LendingDesk_case_03(self):
        self.check(work.LendingDesk, ({'a': 2},), ObjectChecks([('available', ('a',), 2)]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_Library_case_01(self):
        self.check(work.Library, ({'a': 1},), ObjectChecks([('borrow', ('m', 'a'), None), ('loans', ('m',), ['a']), ('available', ('a',), 0), ('return_book', ('m', 'a'), None), ('available', ('a',), 1)]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_Library_case_02(self):
        self.check(work.Library, ({'a': 2},), ObjectChecks([('borrow', ('m', 'a'), None), ('borrow', ('m', 'a'), ValueError), ('available', ('a',), 1)]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_Library_case_03(self):
        self.check(work.Library, ({},), ObjectChecks([('loans', ('x',), []), ('return_book', ('x', 'a'), ValueError), ('borrow', ('x', 'a'), KeyError)]),
                   mode=None, dataclass_required=False,
                   frozen=False)
