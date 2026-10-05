"""Behavioral checks for day 062; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_062_invariants import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_reverse_text_case_01(self):
        self.check(work.reverse_text, ('abc',), 'cba',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_reverse_text_case_02(self):
        self.check(work.reverse_text, ('',), '',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_reverse_text_case_03(self):
        self.check(work.reverse_text, ('été',), 'été',
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_deduplicate_case_01(self):
        self.check(work.deduplicate, ([2, 1, 2, 3],), [2, 1, 3],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_deduplicate_case_02(self):
        self.check(work.deduplicate, ([],), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_deduplicate_case_03(self):
        self.check(work.deduplicate, ([0, 0],), [0],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_encode_runs_case_01(self):
        self.check(work.encode_runs, ('aaabb',), [('a', 3), ('b', 2)],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_encode_runs_case_02(self):
        self.check(work.encode_runs, ('',), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_encode_runs_case_03(self):
        self.check(work.encode_runs, ('aba',), [('a', 1), ('b', 1), ('a', 1)],
                   mode=None, dataclass_required=False,
                   frozen=False)
