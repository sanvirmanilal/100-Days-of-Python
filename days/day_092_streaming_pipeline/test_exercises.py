"""Behavioral checks for day 092; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_092_streaming_pipeline import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_parse_numbers_case_01(self):
        self.check(work.parse_numbers, ([' 1 ', '', '-2'],), [1, -2],
                   mode='iterator', dataclass_required=False,
                   frozen=False)

    def test_01_parse_numbers_case_02(self):
        self.check(work.parse_numbers, ([],), [],
                   mode='iterator', dataclass_required=False,
                   frozen=False)

    def test_01_parse_numbers_case_03(self):
        self.check(work.parse_numbers, (['bad'],), ValueError,
                   mode='iterator', dataclass_required=False,
                   frozen=False)

    def test_02_positive_batches_case_01(self):
        self.check(work.positive_batches, ([-1, 1, 2, 0, 3], 2), [[1, 2], [3]],
                   mode='iterator', dataclass_required=False,
                   frozen=False)

    def test_02_positive_batches_case_02(self):
        self.check(work.positive_batches, ([], 2), [],
                   mode='iterator', dataclass_required=False,
                   frozen=False)

    def test_02_positive_batches_case_03(self):
        self.check(work.positive_batches, ([], 0), ValueError,
                   mode='iterator', dataclass_required=False,
                   frozen=False)

    def test_03_stream_summary_case_01(self):
        self.check(work.stream_summary, (['1', '-2', '3'],), {'count': 3, 'sum': 2, 'min': -2, 'max': 3},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_stream_summary_case_02(self):
        self.check(work.stream_summary, ([' '],), {'count': 0, 'sum': 0, 'min': None, 'max': None},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_stream_summary_case_03(self):
        self.check(work.stream_summary, (['bad'],), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)
