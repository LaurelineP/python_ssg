import unittest

from leafnode import LeafNode
from test_helpers import *

log_test('TestLeafNode')


representation_equal_cases = (
    (
        LeafNode('a', 'the link', {'href': 'https://hello.world'}),
        f"HTMLNode(a, the link, None, {str({ 'href': 'https://hello.world' })})"
    ),
)

to_html_equal_cases = (
    (
        LeafNode('a', 'the link 2', {'href': 'https://hello.world'}).to_html(),
        f'<a href="https://hello.world">the link 2</a>'
    ),
    (
        LeafNode(None, 'the link 3').to_html(),
        f'the link 3'
    ),
)


class TestLeafNode(unittest.TestCase):

    @log_test_with(len(representation_equal_cases))
    def test_repr(self):
        assertEqual(representation_equal_cases, str)

    @log_test_with(len(to_html_equal_cases))
    def test_repr(self):
        assertEqual(to_html_equal_cases, str)


if __name__ == "__main__":
    unittest.main()
