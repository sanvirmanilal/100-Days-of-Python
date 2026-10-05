"""Worked learning example for day 061; independent of the exercises."""

def main():
    import unittest
    class SampleTest(unittest.TestCase):
        def test_empty(self):
            self.assertEqual(len(""), 0)

    print(SampleTest("test_empty").countTestCases())


if __name__ == "__main__":
    main()
