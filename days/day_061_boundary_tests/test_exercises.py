"""Behavioral checks for day 061; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_061_boundary_tests import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_password_length_ok_case_01(self):
        self.check(work.password_length_ok, ('1234567',), False,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_password_length_ok_case_02(self):
        self.check(work.password_length_ok, ('12345678',), True,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_password_length_ok_case_03(self):
        self.check(work.password_length_ok, ('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',), True,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_password_length_ok_case_04(self):
        self.check(work.password_length_ok, ('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',), False,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_ticket_price_case_01(self):
        self.check(work.ticket_price, (4,), 0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_ticket_price_case_02(self):
        self.check(work.ticket_price, (5,), 8,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_ticket_price_case_03(self):
        self.check(work.ticket_price, (18,), 12,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_ticket_price_case_04(self):
        self.check(work.ticket_price, (65,), 6,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_ticket_price_case_05(self):
        self.check(work.ticket_price, (-1,), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_chunk_count_case_01(self):
        self.check(work.chunk_count, (0, 3), 0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_chunk_count_case_02(self):
        self.check(work.chunk_count, (6, 3), 2,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_chunk_count_case_03(self):
        self.check(work.chunk_count, (7, 3), 3,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_chunk_count_case_04(self):
        self.check(work.chunk_count, (1, 0), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)
