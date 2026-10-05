"""Behavioral checks for day 035; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_035_itertools import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_all_pairs_case_01(self):
        self.check(work.all_pairs, ([1, 2, 3],), [(1, 2), (1, 3), (2, 3)],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_all_pairs_case_02(self):
        self.check(work.all_pairs, ([],), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_all_pairs_case_03(self):
        self.check(work.all_pairs, (['a', 'a'],), [('a', 'a')],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_run_lengths_case_01(self):
        self.check(work.run_lengths, (['a', 'a', 'b', 'a'],), [('a', 2), ('b', 1), ('a', 1)],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_run_lengths_case_02(self):
        self.check(work.run_lengths, ([],), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_run_lengths_case_03(self):
        self.check(work.run_lengths, ([1, 1, 1],), [(1, 3)],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_cartesian_product_case_01(self):
        self.check(work.cartesian_product, ([1, 2], ['a', 'b']), [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_cartesian_product_case_02(self):
        self.check(work.cartesian_product, ([], [1]), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_cartesian_product_case_03(self):
        self.check(work.cartesian_product, ([1], []), [],
                   mode=None, dataclass_required=False,
                   frozen=False)
