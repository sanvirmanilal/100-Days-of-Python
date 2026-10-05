"""Behavioral checks for day 082; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_082_binary import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_has_flag_case_01(self):
        self.check(work.has_flag, (10, 2), True,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_has_flag_case_02(self):
        self.check(work.has_flag, (10, 3), False,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_has_flag_case_03(self):
        self.check(work.has_flag, (0, 0), True,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_pack_u16_case_01(self):
        self.check(work.pack_u16, (258,), b'\x01\x02',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_pack_u16_case_02(self):
        self.check(work.pack_u16, (65535,), b'\xff\xff',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_pack_u16_case_03(self):
        self.check(work.pack_u16, (-1,), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_pack_u16_case_04(self):
        self.check(work.pack_u16, (65536,), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_xor_bytes_case_01(self):
        self.check(work.xor_bytes, (b'ABC', 1), b'@CB',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_xor_bytes_case_02(self):
        self.check(work.xor_bytes, (b'', 0), b'',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_xor_bytes_case_03(self):
        self.check(work.xor_bytes, (b'x', 256), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)
