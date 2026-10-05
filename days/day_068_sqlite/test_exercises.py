"""Behavioral checks for day 068; expected failures until you implement the stubs."""
from tests._support import CurriculumCase, File, Database, ObjectChecks
from days.day_068_sqlite import exercises as work


class ExerciseTests(CurriculumCase):
    def test_01_user_names_case_01(self):
        self.check(work.user_names, (Database("CREATE TABLE users(id INTEGER,name TEXT); INSERT INTO users VALUES (2,'Bo'),(1,'Ada');"),), ['Ada', 'Bo'],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_user_names_case_02(self):
        self.check(work.user_names, (Database('CREATE TABLE users(id INTEGER,name TEXT);'),), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_01_user_names_case_03(self):
        self.check(work.user_names, (Database("CREATE TABLE users(id INTEGER,name TEXT); INSERT INTO users VALUES (1,'é');"),), ['é'],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_find_user_case_01(self):
        self.check(work.find_user, (Database("CREATE TABLE users(id INTEGER,name TEXT); INSERT INTO users VALUES (2,'Ada'),(1,'Ada');"), 'Ada'), 1,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_find_user_case_02(self):
        self.check(work.find_user, (Database('CREATE TABLE users(id INTEGER,name TEXT);'), "' OR 1=1 --"), None,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_02_find_user_case_03(self):
        self.check(work.find_user, (Database("CREATE TABLE users(id INTEGER,name TEXT); INSERT INTO users VALUES (1,'Bo');"), 'Ada'), None,
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_score_totals_case_01(self):
        self.check(work.score_totals, (Database("CREATE TABLE scores(name TEXT,points INTEGER); INSERT INTO scores VALUES ('a',2),('a',3),('b',5);"),), [('a', 5), ('b', 5)],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_score_totals_case_02(self):
        self.check(work.score_totals, (Database('CREATE TABLE scores(name TEXT,points INTEGER);'),), [],
                   mode=None, dataclass_required=False,
                   frozen=False)

    def test_03_score_totals_case_03(self):
        self.check(work.score_totals, (Database("CREATE TABLE scores(name TEXT,points INTEGER); INSERT INTO scores VALUES ('x',-1);"),), [('x', -1)],
                   mode=None, dataclass_required=False,
                   frozen=False)
