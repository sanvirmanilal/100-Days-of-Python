"""Behavioral checks for day 076; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_076_hashes import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_sha256_text_case_01(self):
        self.check(work.sha256_text, ('',), 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_sha256_text_case_02(self):
        self.check(work.sha256_text, ('abc',), 'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_sha256_text_case_03(self):
        self.check(work.sha256_text, ('hello',), '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_same_content_case_01(self):
        self.check(work.same_content, (b'a', b'a'), True,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_same_content_case_02(self):
        self.check(work.same_content, (b'a', b'b'), False,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_same_content_case_03(self):
        self.check(work.same_content, (b'', b''), True,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_duplicate_files_case_01(self):
        self.check(work.duplicate_files, ({'b': b'x', 'a': b'x', 'c': b'y'},), [['a', 'b']],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_duplicate_files_case_02(self):
        self.check(work.duplicate_files, ({},), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_duplicate_files_case_03(self):
        self.check(work.duplicate_files, ({'c': b'', 'a': b'', 'd': b'z', 'b': b'z'},), [['a', 'c'], ['b', 'd']],
                   mode=None, dataclass_required=False,
                   frozen=False)
