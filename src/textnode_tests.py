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


log_test('TestDelimitedTextNode')


class TestDelimitedTextNode(unittest.TestCase):

    @log_test_with(len(split_nodes_delimiter_cases))
    def test_representations(self):
        assertEqual(split_nodes_delimiter_cases, str)


log_test('TestDelimiterTextNodeError')


class TestDelimiterTextNodeError(unittest.TestCase):
    @log_test_with(len(split_nodes_delimiter_error_cases))
    def test_errors(self):
        assertRaises(split_nodes_delimiter_error_cases)


log_test('TestExtractMarkdownImages')


class TestExtractMarkdownImages(unittest.TestCase):
    @log_test_with(len(extract_md_images_cases))
    def test_extract_markdown_image(self):
        assertEqual(extract_md_images_cases)


log_test('TestExtractMarkdownLinks')


class TestExtractMarkdownLinks(unittest.TestCase):
    @log_test_with(len(extract_md_links_cases))
    def test_extract_markdown_image(self):
        assertEqual(extract_md_links_cases)


if __name__ == "__main__":
    unittest.main()
