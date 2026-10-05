"""Behavioral checks for day 040; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_040_text_index import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_tokens_case_01(self):
        self.check(work.tokens, ('Python, PYTHON 3!',), ['python', 'python', '3'],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_tokens_case_02(self):
        self.check(work.tokens, ('',), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_tokens_case_03(self):
        self.check(work.tokens, ('a_b',), ['a', 'b'],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_build_index_case_01(self):
        self.check(work.build_index, ({'a': 'Hi hi', 'b': 'hi bye'},), {'hi': {'a', 'b'}, 'bye': {'b'}},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_build_index_case_02(self):
        self.check(work.build_index, ({},), {},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_build_index_case_03(self):
        self.check(work.build_index, ({'a': '!!!'},), {},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_search_case_01(self):
        self.check(work.search, ({'hi': {'a', 'b'}, 'bye': {'b'}}, 'HI bye'), ['b'],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_search_case_02(self):
        self.check(work.search, ({'a': {'x'}}, ''), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_search_case_03(self):
        self.check(work.search, ({'a': {'x'}}, 'missing'), [],
                   mode=None, dataclass_required=False,
                   frozen=False)
