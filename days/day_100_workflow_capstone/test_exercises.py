"""Behavioral checks for day 100; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_100_workflow_capstone import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_ready_tasks_case_01(self):
        self.check(work.ready_tasks, ({'a': [], 'b': ['a'], 'c': []}, ['a']), ['b', 'c'],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_ready_tasks_case_02(self):
        self.check(work.ready_tasks, ({}, []), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_ready_tasks_case_03(self):
        self.check(work.ready_tasks, ({'a': ['b'], 'b': ['a']}, []), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_workflow_layers_case_01(self):
        self.check(work.workflow_layers, ({'a': [], 'b': ['a'], 'c': []},), [['a', 'c'], ['b']],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_workflow_layers_case_02(self):
        self.check(work.workflow_layers, ({},), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_workflow_layers_case_03(self):
        self.check(work.workflow_layers, ({'a': ['a']},), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_workflow_layers_case_04(self):
        self.check(work.workflow_layers, ({'a': ['missing']},), KeyError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_run_workflow_case_01(self):
        self.check(work.run_workflow, ({'a': [], 'b': ['a'], 'c': []}, {'a': False, 'b': True, 'c': True}), {'a': 'failed', 'b': 'blocked', 'c': 'success'},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_run_workflow_case_02(self):
        self.check(work.run_workflow, ({}, {}), {},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_run_workflow_case_03(self):
        self.check(work.run_workflow, ({'a': []}, {}), KeyError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_run_workflow_case_04(self):
        self.check(work.run_workflow, ({'a': ['a']}, {'a': True}), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)
