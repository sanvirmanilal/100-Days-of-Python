"""Behavioral checks for day 022; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_022_regex import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_extract_integers_case_01(self):
        self.check(work.extract_integers, ('a -12 b 3',), [-12, 3],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_extract_integers_case_02(self):
        self.check(work.extract_integers, ('none',), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_extract_integers_case_03(self):
        self.check(work.extract_integers, ('x+4 y007',), [4, 7],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_valid_identifier_case_01(self):
        self.check(work.valid_identifier, ('_x2',), True,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_valid_identifier_case_02(self):
        self.check(work.valid_identifier, ('2x',), False,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_valid_identifier_case_03(self):
        self.check(work.valid_identifier, ('',), False,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_valid_identifier_case_04(self):
        self.check(work.valid_identifier, ('café',), False,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_redact_emails_case_01(self):
        self.check(work.redact_emails, ('Mail a@b.com now',), 'Mail [redacted] now',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_redact_emails_case_02(self):
        self.check(work.redact_emails, ('a@b.com c@d.org',), '[redacted] [redacted]',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_redact_emails_case_03(self):
        self.check(work.redact_emails, ('no email',), 'no email',
                   mode=None, dataclass_required=False,
                   frozen=False)
