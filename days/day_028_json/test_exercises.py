"""Behavioral checks for day 028; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_028_json import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_parse_json_case_01(self):
        self.check(work.parse_json, ('{"a":1}',), {'a': 1},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_parse_json_case_02(self):
        self.check(work.parse_json, ('[true,null]',), [True, None],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_parse_json_case_03(self):
        self.check(work.parse_json, ('oops',), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_canonical_json_case_01(self):
        self.check(work.canonical_json, ({'b': 2, 'a': 'é'},), '{"a":"é","b":2}',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_canonical_json_case_02(self):
        self.check(work.canonical_json, ([],), '[]',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_canonical_json_case_03(self):
        self.check(work.canonical_json, (None,), 'null',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_load_users_case_01(self):
        self.check(work.load_users, ('[{"name":"Ada"},{"name":"Bo"}]',), ['Ada', 'Bo'],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_load_users_case_02(self):
        self.check(work.load_users, ('[]',), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_load_users_case_03(self):
        self.check(work.load_users, ('{}',), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_load_users_case_04(self):
        self.check(work.load_users, ('[{"name":""}]',), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_load_users_case_05(self):
        self.check(work.load_users, ('[{"name":3}]',), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)
