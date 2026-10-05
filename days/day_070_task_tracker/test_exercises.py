"""Behavioral checks for day 070; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_070_task_tracker import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_TaskTracker_case_01(self):
        self.check(work.TaskTracker, (), ObjectChecks([('add', ('read',), 1), ('list_tasks', (), [{'id': 1, 'title': 'read', 'done': False}])]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_TaskTracker_case_02(self):
        self.check(work.TaskTracker, (), ObjectChecks([('add', ('',), ValueError), ('add', ('x',), 1)]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_TaskTracker_case_03(self):
        self.check(work.TaskTracker, (), ObjectChecks([('list_tasks', (), [])]),
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_complete_tasks_case_01(self):
        self.check(work.complete_tasks, ([{'id': 1, 'title': 'x', 'done': False}], [1]), [{'id': 1, 'title': 'x', 'done': True}],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_complete_tasks_case_02(self):
        self.check(work.complete_tasks, ([], []), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_complete_tasks_case_03(self):
        self.check(work.complete_tasks, ([], [1]), KeyError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_task_report_case_01(self):
        self.check(work.task_report, ([{'title': 'b', 'done': False}, {'title': 'a', 'done': True}],), {'total': 2, 'completed': 1, 'pending': ['b']},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_task_report_case_02(self):
        self.check(work.task_report, ([],), {'total': 0, 'completed': 0, 'pending': []},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_task_report_case_03(self):
        self.check(work.task_report, ([{'title': 'z', 'done': False}, {'title': 'a', 'done': False}],), {'total': 2, 'completed': 0, 'pending': ['a', 'z']},
                   mode=None, dataclass_required=False,
                   frozen=False)
