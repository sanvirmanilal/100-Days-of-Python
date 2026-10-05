"""Behavioral checks for day 017; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_017_exceptions import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_parse_integer_case_01(self):
        self.check(work.parse_integer, ('  -12 ',), -12,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_parse_integer_case_02(self):
        self.check(work.parse_integer, ('2.5',), None,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_parse_integer_case_03(self):
        self.check(work.parse_integer, ('',), None,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_divide_case_01(self):
        self.check(work.divide, (6, 3), 2.0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_divide_case_02(self):
        self.check(work.divide, (0, 2), 0.0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_divide_case_03(self):
        self.check(work.divide, (1, 0), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_require_keys_case_01(self):
        self.check(work.require_keys, ({'a': 1, 'b': 2}, ['b']), {'b': 2},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_require_keys_case_02(self):
        self.check(work.require_keys, ({}, []), {},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_require_keys_case_03(self):
        self.check(work.require_keys, ({'a': None}, ['a']), {'a': None},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_require_keys_case_04(self):
        self.check(work.require_keys, ({}, ['x']), KeyError,
                   mode=None, dataclass_required=False,
                   frozen=False)
