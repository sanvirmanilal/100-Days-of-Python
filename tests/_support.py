"""Test fixtures and assertions. No exercise implementations live here."""
import asyncio
import copy
import inspect
import io
import sqlite3
import shutil
from uuid import uuid4
import unittest
from contextlib import redirect_stderr
from dataclasses import dataclass, is_dataclass, FrozenInstanceError
from pathlib import Path
from unittest.mock import Mock


@dataclass
class File:
    content: str


@dataclass
class Database:
    script: str


@dataclass
class ObjectChecks:
    steps: list


def raise_value(*args, **kwargs):
    raise ValueError('Injected test failure')


def always_missing(*args):
    raise KeyError('Injected missing value')


def print_ready():
    print('ready')


class CurriculumCase(unittest.TestCase):
    def setUp(self):
        self._temporary = None
        self._file_number = 0

    def realize(self, value):
        if isinstance(value, File):
            if self._temporary is None:
                scratch = Path(__file__).resolve().parents[1] / '.practice_tmp'
                scratch.mkdir(exist_ok=True)
                self._temporary = scratch / f'case_{uuid4().hex}'
                self._temporary.mkdir()
                def cleanup():
                    target = self._temporary.resolve()
                    if target.parent != scratch.resolve() or not target.name.startswith('case_'):
                        raise ValueError('Fixture cleanup must stay inside the scratch folder')
                    shutil.rmtree(target)
                self.addCleanup(cleanup)
            self._file_number += 1
            path = self._temporary / f'input_{self._file_number}.txt'
            path.write_text(value.content, encoding='utf-8')
            return path
        if isinstance(value, Database):
            connection = sqlite3.connect(':memory:')
            self.addCleanup(connection.close)
            connection.executescript(value.script)
            return connection
        if isinstance(value, str) and value.startswith('CALL:'):
            callbacks = {
                'int': int, 'str': str, 'abs': abs, 'bool': bool, 'float': float,
                'str.upper': str.upper, 'str.strip': str.strip, 'str.isupper': str.isupper,
                'print_ready': print_ready, 'print_nothing': lambda: None,
                'raise_value': raise_value, 'read_x': lambda mapping: mapping['x'],
                'clock_100': lambda: 100, 'clock_0': lambda: 0,
                'lookup_zero': lambda key: {'x': 0}[key], 'always_missing': always_missing,
                'noop': lambda *args: None,
            }
            return Mock(side_effect=callbacks[value[5:]])
        if isinstance(value, list):
            return [self.realize(item) for item in value]
        if isinstance(value, tuple):
            return tuple(self.realize(item) for item in value)
        if isinstance(value, dict):
            return {key: self.realize(item) for key, item in value.items()}
        return value

    def assert_value(self, actual, expected):
        if isinstance(expected, float):
            self.assertIsInstance(actual, (int, float))
            self.assertAlmostEqual(actual, expected, places=8)
        elif isinstance(expected, (list, tuple)):
            self.assertIsInstance(actual, type(expected))
            self.assertEqual(len(actual), len(expected))
            for left, right in zip(actual, expected):
                self.assert_value(left, right)
        elif isinstance(expected, dict):
            self.assertIsInstance(actual, dict)
            self.assertEqual(actual.keys(), expected.keys())
            for key in expected:
                self.assert_value(actual[key], expected[key])
        else:
            if isinstance(expected, bool):
                self.assertIsInstance(actual, bool)
            self.assertEqual(actual, expected)

    @staticmethod
    def is_exception(value):
        return isinstance(value, type) and issubclass(value, BaseException)

    def check(self, function, original_args, expected, mode=None, dataclass_required=False, frozen=False):
        args = self.realize(original_args)
        # All curriculum contracts leave caller-owned collections unchanged.
        snapshots = [(index, copy.deepcopy(arg)) for index, arg in enumerate(args)
                     if isinstance(arg, (list, dict, set)) and not self.contains_callable(arg)]

        def invoke():
            if mode == 'async':
                self.assertTrue(inspect.iscoroutinefunction(function), 'Use async def')
                return asyncio.run(function(*args))
            actual = function(*args)
            if mode == 'iterator':
                self.assertIs(iter(actual), actual, 'Return an iterator, not an eager collection')
                return list(actual)
            return actual

        try:
            # argparse deliberately prints usage before SystemExit; keep test output focused.
            with redirect_stderr(io.StringIO()):
                if self.is_exception(expected):
                    with self.assertRaises(expected):
                        invoke()
                elif isinstance(expected, ObjectChecks):
                    obj = invoke()
                    if dataclass_required:
                        self.assertTrue(is_dataclass(obj), 'Implement a dataclass')
                    for method, method_args, result in expected.steps:
                        def operation():
                            if method.startswith('@'):
                                return getattr(obj, method[1:])
                            if method == '!list':
                                return list(obj)
                            return getattr(obj, method)(*self.realize(method_args))
                        if self.is_exception(result):
                            with self.assertRaises(result):
                                operation()
                        else:
                            self.assert_value(operation(), result)
                    if frozen:
                        field = next(iter(obj.__dataclass_fields__))
                        with self.assertRaises(FrozenInstanceError):
                            setattr(obj, field, getattr(obj, field))
                else:
                    self.assert_value(invoke(), expected)
        finally:
            for index, snapshot in snapshots:
                self.assertEqual(args[index], snapshot, 'Do not mutate caller-owned input')
        if function.__name__ == 'stamp' and not self.is_exception(expected):
            args[1].assert_called_once_with()
        if function.__name__ == 'notify_all' and not self.is_exception(expected):
            self.assertEqual([call.args for call in args[1].call_args_list], [(name,) for name in args[0]])

    def contains_callable(self, value):
        if callable(value):
            return True
        if isinstance(value, dict):
            return any(self.contains_callable(item) for item in value.values())
        if isinstance(value, (list, tuple, set)):
            return any(self.contains_callable(item) for item in value)
        return False
