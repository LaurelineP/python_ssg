import unittest

from htmlnode_cases import *
from test_helpers import *

log_test('TestHTMLNode')


class TestHTMLNode(unittest.TestCase):
    @log_test_with(len(representation_equal_cases))
    def test_representation_test(self):
        assertEqual(representation_equal_cases, str)

    @log_test_with(len(raise_error_cases))
    def test_raise_errors(self):
        assertEqual(raise_error_cases)


log_test('TestLeafNode')


class TestLeafNode(unittest.TestCase):

    @log_test_with(len(leaf_node_representation_equal_cases))
    def test_repr(self):
        assertEqual(leaf_node_representation_equal_cases, str)

    @log_test_with(len(leafNode_to_html_equal_cases))
    def test_repr(self):
        assertEqual(leafNode_to_html_equal_cases, str)


log_test('TestParentNode')


class TestParentNode(unittest.TestCase):
    @log_test_with(len(parentNode_to_html_cases))
    def test_to_html(self):
        assertEqual(parentNode_to_html_cases, str)


if __name__ == "__main__":
    unittest.main()
