"""Behavioral checks for day 006; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_006_loops import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_sum_to_case_01(self):
        self.check(work.sum_to, (0,), 0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_sum_to_case_02(self):
        self.check(work.sum_to, (1,), 1,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_sum_to_case_03(self):
        self.check(work.sum_to, (5,), 15,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_count_multiples_case_01(self):
        self.check(work.count_multiples, (10, 3), 3,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_count_multiples_case_02(self):
        self.check(work.count_multiples, (0, 2), 0,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_count_multiples_case_03(self):
        self.check(work.count_multiples, (6, 1), 6,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_fizzbuzz_case_01(self):
        self.check(work.fizzbuzz, (0,), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_fizzbuzz_case_02(self):
        self.check(work.fizzbuzz, (5,), ['1', '2', 'Fizz', '4', 'Buzz'],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_fizzbuzz_case_03(self):
        self.check(work.fizzbuzz, (15,), ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz'],
                   mode=None, dataclass_required=False,
                   frozen=False)
