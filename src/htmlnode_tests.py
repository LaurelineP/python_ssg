import unittest

from htmlnode import HTMLNode
from test_helpers import *

representation_equal_cases = (
    (
        HTMLNode(),
        'HTMLNode(None, None, None, None)'
    ),
    (
        HTMLNode('a'),
        'HTMLNode(a, None, None, None)'
    ),
    (
        HTMLNode('a', 'the link'),
        'HTMLNode(a, the link, None, None)'
    ),
    (
        HTMLNode('a', 'the link', ['hello', 'word']),
        "HTMLNode(a, the link, ['hello', 'word'], None)"
    ),
    (
        HTMLNode('a', 'the link', ['hello', 'word'],
                 {'href': 'https://hello.world'}),
        "HTMLNode(a, the link, ['hello', 'word'], {'href': 'https://hello.world'})"
    ),
)

raise_error_cases = (
    (
        HTMLNode(
            'a',
            'the link',
            ['hello', 'word'],
            {'href': 'https://hello.world'}
        ).props_to_html(),
        ' href="https://hello.world"'
    ),
)

log_test('TestHTMLNode')


class TestHTMLNode(unittest.TestCase):
    @log_test_with(len(representation_equal_cases))
    def test_representation_test(self):
        assertEqual(representation_equal_cases, str)

    @log_test_with(len(raise_error_cases))
    def test_raise_errors(self):
        assertEqual(raise_error_cases)


if __name__ == "__main__":
    unittest.main()
