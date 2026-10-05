"""Behavioral checks for day 069; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_069_sql_relations import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_task_owners_case_01(self):
        self.check(work.task_owners, (Database("CREATE TABLE users(id INTEGER,name TEXT); CREATE TABLE tasks(id INTEGER,user_id INTEGER,done INTEGER);INSERT INTO users VALUES (1,'Ada'); INSERT INTO tasks VALUES (2,1,0),(3,9,0);"),), [(2, 'Ada')],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_task_owners_case_02(self):
        self.check(work.task_owners, (Database('CREATE TABLE users(id INTEGER,name TEXT); CREATE TABLE tasks(id INTEGER,user_id INTEGER,done INTEGER);'),), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_task_owners_case_03(self):
        self.check(work.task_owners, (Database('CREATE TABLE users(id INTEGER,name TEXT); CREATE TABLE tasks(id INTEGER,user_id INTEGER,done INTEGER);INSERT INTO tasks VALUES (1,9,0);'),), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_user_task_counts_case_01(self):
        self.check(work.user_task_counts, (Database("CREATE TABLE users(id INTEGER,name TEXT); CREATE TABLE tasks(id INTEGER,user_id INTEGER,done INTEGER);INSERT INTO users VALUES (1,'A'),(2,'B'); INSERT INTO tasks VALUES (1,1,0),(2,1,1);"),), [(1, 2), (2, 0)],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_user_task_counts_case_02(self):
        self.check(work.user_task_counts, (Database('CREATE TABLE users(id INTEGER,name TEXT); CREATE TABLE tasks(id INTEGER,user_id INTEGER,done INTEGER);'),), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_user_task_counts_case_03(self):
        self.check(work.user_task_counts, (Database("CREATE TABLE users(id INTEGER,name TEXT); CREATE TABLE tasks(id INTEGER,user_id INTEGER,done INTEGER);INSERT INTO users VALUES (3,'C');"),), [(3, 0)],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_completion_rates_case_01(self):
        self.check(work.completion_rates, (Database("CREATE TABLE users(id INTEGER,name TEXT); CREATE TABLE tasks(id INTEGER,user_id INTEGER,done INTEGER);INSERT INTO users VALUES (1,'A'),(2,'B'); INSERT INTO tasks VALUES (1,1,0),(2,1,1);"),), [(1, 0.5), (2, 0.0)],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_completion_rates_case_02(self):
        self.check(work.completion_rates, (Database('CREATE TABLE users(id INTEGER,name TEXT); CREATE TABLE tasks(id INTEGER,user_id INTEGER,done INTEGER);'),), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_completion_rates_case_03(self):
        self.check(work.completion_rates, (Database("CREATE TABLE users(id INTEGER,name TEXT); CREATE TABLE tasks(id INTEGER,user_id INTEGER,done INTEGER);INSERT INTO users VALUES (1,'A'); INSERT INTO tasks VALUES (1,1,1);"),), [(1, 1.0)],
                   mode=None, dataclass_required=False,
                   frozen=False)
