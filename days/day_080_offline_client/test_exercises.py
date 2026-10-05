"""Behavioral checks for day 080; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_080_offline_client import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_unwrap_response_case_01(self):
        self.check(work.unwrap_response, ({'status': 200, 'body': {'items': [1], 'next': None}},), {'items': [1], 'next': None},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_unwrap_response_case_02(self):
        self.check(work.unwrap_response, ({'status': 500, 'body': {}},), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_unwrap_response_case_03(self):
        self.check(work.unwrap_response, ({'status': 200, 'body': {'items': [], 'next': 2}},), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_fetch_all_case_01(self):
        self.check(work.fetch_all, ({'a': {'status': 200, 'body': {'items': [1], 'next': 'b'}}, 'b': {'status': 200, 'body': {'items': [2], 'next': None}}}, 'a'), [1, 2],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_fetch_all_case_02(self):
        self.check(work.fetch_all, ({}, 'a'), KeyError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_fetch_all_case_03(self):
        self.check(work.fetch_all, ({'a': {'status': 200, 'body': {'items': [], 'next': 'a'}}}, 'a'), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_sync_items_case_01(self):
        self.check(work.sync_items, ({'a': {'status': 200, 'body': {'items': [{'id': 2, 'name': 'old'}, {'id': 1, 'name': 'a'}, {'id': 2, 'name': 'new'}], 'next': None}}}, 'a'), [{'id': 1, 'name': 'a'}, {'id': 2, 'name': 'new'}],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_sync_items_case_02(self):
        self.check(work.sync_items, ({'a': {'status': 200, 'body': {'items': [], 'next': None}}}, 'a'), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_sync_items_case_03(self):
        self.check(work.sync_items, ({'a': {'status': 200, 'body': {'items': [{'id': 0, 'name': 'x'}], 'next': None}}}, 'a'), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)
