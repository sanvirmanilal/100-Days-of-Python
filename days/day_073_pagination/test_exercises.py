"""Behavioral checks for day 073; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_073_pagination import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_page_case_01(self):
        self.check(work.page, ([1, 2, 3], 1, 2), [2, 3],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_page_case_02(self):
        self.check(work.page, ([], 0, 3), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_page_case_03(self):
        self.check(work.page, ([1], 0, 0), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_paginate_case_01(self):
        self.check(work.paginate, ([1, 2, 3], 2), [{'items': [1, 2], 'next_offset': 2}, {'items': [3], 'next_offset': None}],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_paginate_case_02(self):
        self.check(work.paginate, ([], 1), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_paginate_case_03(self):
        self.check(work.paginate, ([], 0), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_collect_pages_case_01(self):
        self.check(work.collect_pages, ({'a': {'items': [1], 'next': 'b'}, 'b': {'items': [2], 'next': None}}, 'a'), [1, 2],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_collect_pages_case_02(self):
        self.check(work.collect_pages, ({'a': {'items': [], 'next': 'a'}}, 'a'), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_collect_pages_case_03(self):
        self.check(work.collect_pages, ({}, 'x'), KeyError,
                   mode=None, dataclass_required=False,
                   frozen=False)
