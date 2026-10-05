"""Behavioral checks for day 075; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_075_caching import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_fresh_case_01(self):
        self.check(work.fresh, ({'expires': 10}, 9), True,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_fresh_case_02(self):
        self.check(work.fresh, ({'expires': 10}, 10), False,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_fresh_case_03(self):
        self.check(work.fresh, ({'expires': 0}, 1), False,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_cache_get_case_01(self):
        self.check(work.cache_get, ({'x': {'value': 0, 'expires': 10}}, 'x', 9), 0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_cache_get_case_02(self):
        self.check(work.cache_get, ({}, 'x', 0), None,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_cache_get_case_03(self):
        self.check(work.cache_get, ({'x': {'value': 3, 'expires': 10}}, 'x', 10), None,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_LRUCache_case_01(self):
        self.check(work.LRUCache, (2,), ObjectChecks([('put', ('a', 1), None), ('put', ('b', 2), None), ('get', ('a',), 1), ('put', ('c', 3), None), ('keys', (), ['a', 'c']), ('get', ('b',), None)]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_LRUCache_case_02(self):
        self.check(work.LRUCache, (1,), ObjectChecks([('put', ('a', 1), None), ('put', ('a', 2), None), ('get', ('a',), 2)]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_LRUCache_case_03(self):
        self.check(work.LRUCache, (0,), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)
