"""Verify grading mechanics without implementing any assignments."""
import asyncio
import unittest
from dataclasses import dataclass
from ._support import CurriculumCase, File, Database, ObjectChecks


class SupportTests(CurriculumCase):
    def test_expected_errors_are_required(self):
        with self.assertRaises(AssertionError):
            self.check(lambda: None, (), ValueError)

    def test_wrong_answers_fail(self):
        with self.assertRaises(AssertionError):
            self.check(lambda: 'wrong', (), 'expected')

    def test_floats_inside_nested_results(self):
        self.assert_value({'x': [(1, 0.1 + 0.2)]}, {'x': [(1, 0.3)]})

    def test_booleans_are_not_integers(self):
        with self.assertRaises(AssertionError):
            self.assert_value(1, True)

    def test_detects_input_mutation(self):
        def mutate(values):
            values.append('unexpected')
        with self.assertRaises(AssertionError):
            self.check(mutate, ([],), None)

    def test_iterator_mode_rejects_lists(self):
        with self.assertRaises(AssertionError):
            self.check(lambda: [], (), [], mode='iterator')

    def test_iterator_mode_accepts_iterators(self):
        self.check(lambda: iter(['sample']), (), ['sample'], mode='iterator')

    def test_async_mode_runs_coroutine(self):
        async def sample():
            await asyncio.sleep(0)
            return 'sample'
        self.check(sample, (), 'sample', mode='async')

    def test_utf8_file_fixture(self):
        path = self.realize(File('é\n'))
        self.assertEqual(path.read_text(encoding='utf-8'), 'é\n')

    def test_in_memory_database_fixture(self):
        connection = self.realize(Database('CREATE TABLE sample(value INTEGER); INSERT INTO sample VALUES (7);'))
        self.assertEqual(connection.execute('SELECT value FROM sample').fetchone(), (7,))

    def test_object_and_frozen_dataclass_checks(self):
        @dataclass(frozen=True)
        class Sample:
            text: str
        self.check(Sample, ('sample',), ObjectChecks([('@text', (), 'sample')]),
                   dataclass_required=True, frozen=True)

    def test_callbacks_record_calls(self):
        callback = self.realize('CALL:clock_100')
        self.assertEqual(callback(), 100)
        callback.assert_called_once_with()
