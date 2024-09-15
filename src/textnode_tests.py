import unittest

from test_helpers import *
from textnode import *
from textnode_cases import *

log_test('TestTextNode')


class TestTextNode(unittest.TestCase):
    @log_test_with(len(equal_cases_OK + equal_cases_NOK))
    def test_equality(self):
        for test_case in equal_cases_OK:
            self.assertEqual(*test_case[0])

        for test_case in equal_cases_NOK:
            self.assertNotEqual(*test_case[0])

    @log_test_with(len(repr_cases_OK))
    def test_representation(self):
        for test_case in repr_cases_OK:
            self.assertEqual(test_case[0].__repr__(), test_case[1])


log_test('TestTextNodeToHTML')


class TestTextNodeToHTML(unittest.TestCase):

    @log_test_with(len(textnode_to_html))
    def test_representation(self):
        assertEqual(textnode_to_html)


if __name__ == "__main__":
    unittest.main()
