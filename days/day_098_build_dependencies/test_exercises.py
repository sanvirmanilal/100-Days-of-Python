"""Behavioral checks for day 098; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_098_build_dependencies import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_dependency_closure_case_01(self):
        self.check(work.dependency_closure, ({'a': ['b'], 'b': ['c']}, 'a'), {'b', 'c'},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_dependency_closure_case_02(self):
        self.check(work.dependency_closure, ({}, 'x'), set(),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_dependency_closure_case_03(self):
        self.check(work.dependency_closure, ({'a': ['a']}, 'a'), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_build_plan_case_01(self):
        self.check(work.build_plan, ({'app': ['test', 'compile'], 'test': ['compile'], 'compile': []}, 'app'), ['compile', 'test', 'app'],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_build_plan_case_02(self):
        self.check(work.build_plan, ({}, 'x'), ['x'],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_build_plan_case_03(self):
        self.check(work.build_plan, ({'a': ['b'], 'b': ['a']}, 'a'), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_affected_targets_case_01(self):
        self.check(work.affected_targets, ({'app': ['lib'], 'test': ['lib'], 'lib': ['base']}, ['base']), ['app', 'base', 'lib', 'test'],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_affected_targets_case_02(self):
        self.check(work.affected_targets, ({}, ['x']), ['x'],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_affected_targets_case_03(self):
        self.check(work.affected_targets, ({'a': ['b'], 'b': ['a']}, ['a']), ['a', 'b'],
                   mode=None, dataclass_required=False,
                   frozen=False)
