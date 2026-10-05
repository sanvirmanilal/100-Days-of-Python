"""Behavioral checks for day 023; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_023_parsing import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_parse_pair_case_01(self):
        self.check(work.parse_pair, (' a = b=c ',), ('a', 'b=c'),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_parse_pair_case_02(self):
        self.check(work.parse_pair, ('x=',), ('x', ''),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_parse_pair_case_03(self):
        self.check(work.parse_pair, ('oops',), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_parse_pair_case_04(self):
        self.check(work.parse_pair, ('=x',), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_parse_config_case_01(self):
        self.check(work.parse_config, ('# hi\na=1\na=2\nb=x',), {'a': '2', 'b': 'x'},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_parse_config_case_02(self):
        self.check(work.parse_config, ('',), {},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_parse_config_case_03(self):
        self.check(work.parse_config, ('bad',), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_parse_ranges_case_01(self):
        self.check(work.parse_ranges, ('1, 3-5,3',), [1, 3, 4, 5],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_parse_ranges_case_02(self):
        self.check(work.parse_ranges, ('',), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_parse_ranges_case_03(self):
        self.check(work.parse_ranges, ('5-2',), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_parse_ranges_case_04(self):
        self.check(work.parse_ranges, ('0',), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_parse_ranges_case_05(self):
        self.check(work.parse_ranges, ('1,',), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)
