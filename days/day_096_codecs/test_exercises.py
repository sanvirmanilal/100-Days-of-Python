"""Behavioral checks for day 096; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_096_codecs import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_to_base64_case_01(self):
        self.check(work.to_base64, (b'hello',), 'aGVsbG8=',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_to_base64_case_02(self):
        self.check(work.to_base64, (b'',), '',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_to_base64_case_03(self):
        self.check(work.to_base64, (b'\x00\xff',), 'AP8=',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_from_base64_case_01(self):
        self.check(work.from_base64, ('aGVsbG8=',), b'hello',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_from_base64_case_02(self):
        self.check(work.from_base64, ('',), b'',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_from_base64_case_03(self):
        self.check(work.from_base64, ('@@@',), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_decode_frames_case_01(self):
        self.check(work.decode_frames, (b'\x00\x02hi\x00\x00',), [b'hi', b''],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_decode_frames_case_02(self):
        self.check(work.decode_frames, (b'',), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_decode_frames_case_03(self):
        self.check(work.decode_frames, (b'\x00\x03hi',), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_decode_frames_case_04(self):
        self.check(work.decode_frames, (b'\x00',), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)
