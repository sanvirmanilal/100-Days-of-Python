"""Behavioral checks for day 042; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_042_dataclasses import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_Point_case_01(self):
        self.check(work.Point, (3, 4), ObjectChecks([('@x', (), 3), ('@y', (), 4), ('distance_from_origin', (), 5.0)]),
                   mode=None, dataclass_required=True,
                   frozen=True)

    def test_01_Point_case_02(self):
        self.check(work.Point, (0, 0), ObjectChecks([('distance_from_origin', (), 0.0)]),
                   mode=None, dataclass_required=True,
                   frozen=True)

    def test_01_Point_case_03(self):
        self.check(work.Point, (-3, 4), ObjectChecks([('distance_from_origin', (), 5.0)]),
                   mode=None, dataclass_required=True,
                   frozen=True)

    def test_02_Product_case_01(self):
        self.check(work.Product, ('tea', 250), ObjectChecks([('@name', (), 'tea'), ('total', (3,), 750), ('total', (-1,), ValueError)]),
                   mode=None, dataclass_required=True,
                   frozen=True)

    def test_02_Product_case_02(self):
        self.check(work.Product, ('', 10), ValueError,
                   mode=None, dataclass_required=True,
                   frozen=True)

    def test_02_Product_case_03(self):
        self.check(work.Product, ('x', -1), ValueError,
                   mode=None, dataclass_required=True,
                   frozen=True)

    def test_03_TodoList_case_01(self):
        self.check(work.TodoList, (), ObjectChecks([('pending', (), []), ('add', ('read',), None), ('pending', (), ['read'])]),
                   mode=None, dataclass_required=True,
                   frozen=False)

    def test_03_TodoList_case_02(self):
        self.check(work.TodoList, (), ObjectChecks([('add', ('code',), None), ('add', ('test',), None), ('pending', (), ['code', 'test'])]),
                   mode=None, dataclass_required=True,
                   frozen=False)

    def test_03_TodoList_case_03(self):
        self.check(work.TodoList, (), ObjectChecks([('pending', (), [])]),
                   mode=None, dataclass_required=True,
                   frozen=False)
