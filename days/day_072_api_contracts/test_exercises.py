"""Behavioral checks for day 072; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_072_api_contracts import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_valid_status_case_01(self):
        self.check(work.valid_status, (200,), True,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_valid_status_case_02(self):
        self.check(work.valid_status, (299,), True,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_valid_status_case_03(self):
        self.check(work.valid_status, (300,), False,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_valid_status_case_04(self):
        self.check(work.valid_status, (True,), False,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_validate_item_case_01(self):
        self.check(work.validate_item, ({'id': 1, 'name': 'a', 'x': 2},), {'id': 1, 'name': 'a'},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_validate_item_case_02(self):
        self.check(work.validate_item, ({'id': True, 'name': 'a'},), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_validate_item_case_03(self):
        self.check(work.validate_item, ({'id': 1, 'name': ''},), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_decode_response_case_01(self):
        self.check(work.decode_response, (200, '{"items":[{"id":1,"name":"a"}]}'), [{'id': 1, 'name': 'a'}],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_decode_response_case_02(self):
        self.check(work.decode_response, (204, '{"items":[]}'), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_decode_response_case_03(self):
        self.check(work.decode_response, (404, '{}'), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_decode_response_case_04(self):
        self.check(work.decode_response, (200, '{"items":{}}'), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)
