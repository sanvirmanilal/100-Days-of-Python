"""Behavioral checks for day 091; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_091_schema_migrations import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_migrate_user_case_01(self):
        self.check(work.migrate_user, ({'version': 1, 'name': 'Ada'},), {'version': 2, 'display_name': 'Ada'},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_migrate_user_case_02(self):
        self.check(work.migrate_user, ({'version': 2, 'display_name': 'Bo', 'extra': 1},), {'version': 2, 'display_name': 'Bo'},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_migrate_user_case_03(self):
        self.check(work.migrate_user, ({'version': 3},), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_migrate_user_case_04(self):
        self.check(work.migrate_user, ({'version': True, 'name': 'A'},), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_migrate_users_case_01(self):
        self.check(work.migrate_users, ([{'version': 1, 'name': 'A'}],), [{'version': 2, 'display_name': 'A'}],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_migrate_users_case_02(self):
        self.check(work.migrate_users, ([],), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_migrate_users_case_03(self):
        self.check(work.migrate_users, ([{'version': 1, 'name': ''}],), ValueError,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_migration_report_case_01(self):
        self.check(work.migration_report, ([{'version': 1, 'name': 'A'}, {'version': 9}, {'version': 2, 'display_name': 'B'}],), {'users': [{'version': 2, 'display_name': 'A'}, {'version': 2, 'display_name': 'B'}], 'errors': [1]},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_migration_report_case_02(self):
        self.check(work.migration_report, ([],), {'users': [], 'errors': []},
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_migration_report_case_03(self):
        self.check(work.migration_report, ([{}],), {'users': [], 'errors': [0]},
                   mode=None, dataclass_required=False,
                   frozen=False)
