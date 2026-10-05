"""Behavioral checks for day 071; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_071_urls import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_url_host_case_01(self):
        self.check(work.url_host, ('https://EXAMPLE.test:443/a',), 'example.test',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_url_host_case_02(self):
        self.check(work.url_host, ('/relative',), None,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_url_host_case_03(self):
        self.check(work.url_host, ('http://localhost/',), 'localhost',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_query_values_case_01(self):
        self.check(work.query_values, ('https://x.test/?a=1&a=2&b=',), {'a': ['1', '2'], 'b': ['']},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_query_values_case_02(self):
        self.check(work.query_values, ('/path',), {},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_query_values_case_03(self):
        self.check(work.query_values, ('/?q=hello+world',), {'q': ['hello world']},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_build_url_case_01(self):
        self.check(work.build_url, ('https://x.test/a', {'q': 'a b', 'tag': ['x', 'y']}), 'https://x.test/a?q=a+b&tag=x&tag=y',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_build_url_case_02(self):
        self.check(work.build_url, ('/a', {}), '/a',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_build_url_case_03(self):
        self.check(work.build_url, ('/a', {'x': '&'}), '/a?x=%26',
                   mode=None, dataclass_required=False,
                   frozen=False)
