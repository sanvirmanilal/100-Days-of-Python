"""Behavioral checks for day 083; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_083_matrices import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_matrix_shape_case_01(self):
        self.check(work.matrix_shape, ([[1, 2], [3, 4]],), (2, 2),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_matrix_shape_case_02(self):
        self.check(work.matrix_shape, ([],), (0, 0),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_matrix_shape_case_03(self):
        self.check(work.matrix_shape, ([[1], [2, 3]],), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_matrix_shape_case_04(self):
        self.check(work.matrix_shape, ([[]],), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_transpose_case_01(self):
        self.check(work.transpose, ([[1, 2, 3], [4, 5, 6]],), [[1, 4], [2, 5], [3, 6]],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_transpose_case_02(self):
        self.check(work.transpose, ([],), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_transpose_case_03(self):
        self.check(work.transpose, ([[1], [2, 3]],), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_matrix_multiply_case_01(self):
        self.check(work.matrix_multiply, ([[1, 2]], [[3], [4]]), [[11]],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_matrix_multiply_case_02(self):
        self.check(work.matrix_multiply, ([], []), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_matrix_multiply_case_03(self):
        self.check(work.matrix_multiply, ([[1, 2]], [[1, 2]]), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_matrix_multiply_case_04(self):
        self.check(work.matrix_multiply, ([[1]], []), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)
