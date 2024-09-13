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
        HTMLNode('a', 'the link', ['hello', 'word'],
                 {'href': 'https://hello.world'}).props_to_html,
        ''
    )
)

log_test('TestHTMLNode')


class TestHTMLNode(unittest.TestCase):
    @log_test_with(len(representation_equal_cases))
    def test_representation_test(self):
        for case in representation_equal_cases:
            self.assertEqual(str(case[0]), case[1])

    @log_test_with(len(raise_error_cases))
    def test_raise_errors(self):
        for case in representation_equal_cases:
            self.assertEqual(str(case[0]), case[1])


if __name__ == "__main__":
    unittest.main()
