"""Behavioral checks for day 018; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_018_nested_data import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_names_case_01(self):
        self.check(work.names, ([{'name': 'Ada'}, {'name': 'Bo'}],), ['Ada', 'Bo'],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_names_case_02(self):
        self.check(work.names, ([],), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_names_case_03(self):
        self.check(work.names, ([{'name': ''}],), [''],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_group_by_case_01(self):
        self.check(work.group_by, ([{'k': 'a', 'v': 1}, {'k': 'a', 'v': 2}], 'k'), {'a': [{'k': 'a', 'v': 1}, {'k': 'a', 'v': 2}]},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_group_by_case_02(self):
        self.check(work.group_by, ([], 'x'), {},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_group_by_case_03(self):
        self.check(work.group_by, ([{'k': 1}, {'k': 2}], 'k'), {1: [{'k': 1}], 2: [{'k': 2}]},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_get_nested_case_01(self):
        self.check(work.get_nested, ({'a': {'b': 2}}, ['a', 'b']), 2,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_get_nested_case_02(self):
        self.check(work.get_nested, ({'a': None}, ['a', 'b'], 'missing'), 'missing',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_get_nested_case_03(self):
        self.check(work.get_nested, ({}, [], 0), {},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_get_nested_case_04(self):
        self.check(work.get_nested, ({}, ['x']), None,
                   mode=None, dataclass_required=False,
                   frozen=False)
