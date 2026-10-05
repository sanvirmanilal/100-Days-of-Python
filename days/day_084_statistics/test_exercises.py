"""Behavioral checks for day 084; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_084_statistics import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_mean_case_01(self):
        self.check(work.mean, ([1, 2, 3],), 2.0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_mean_case_02(self):
        self.check(work.mean, ([0],), 0.0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_mean_case_03(self):
        self.check(work.mean, ([],), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_median_case_01(self):
        self.check(work.median, ([3, 1, 2],), 2,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_median_case_02(self):
        self.check(work.median, ([4, 1, 2, 3],), 2.5,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_median_case_03(self):
        self.check(work.median, ([],), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_population_variance_case_01(self):
        self.check(work.population_variance, ([1, 2, 3],), 0.6666666666666666,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_population_variance_case_02(self):
        self.check(work.population_variance, ([4],), 0.0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_population_variance_case_03(self):
        self.check(work.population_variance, ([],), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)
