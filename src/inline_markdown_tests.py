import unittest

from inline_markdown import *
from inline_markdown_cases import *
from test_helpers import *

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


log_test('TestSplitNodes')


class TestSplitNodes(unittest.TestCase):
    @log_test_with(len(split_images_and_links_cases))
    def test_split_text_nodes(self):
        assertEqual(split_images_and_links_cases, str)
