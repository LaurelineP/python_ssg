import unittest

from leafnode import LeafNode
from parentNode import ParentNode
from test_helpers import *

to_html_cases = (
    (
        ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        ).to_html(),
        '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
    ),
)


log_test('TestParentNode')


class TestParentNode(unittest.TestCase):
    @log_test_with(len(to_html_cases))
    def test_to_html(self):
        assertEqual(to_html_cases, str)


if __name__ == "__main__":
    unittest.main()
