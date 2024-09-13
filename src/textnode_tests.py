import unittest

from test_helpers import log_test, log_test_with
from textnode import TextNode

# -------------------------------- EQUAL CASES ------------------------------- #
equal_intro_case = (
    (
        # equal test: 2 same args for each - no third arg
        (
            TextNode("This is a text node", "bold"),
            TextNode("This is a text node", "bold")
        ),
    ),
)
equal_cases_OK = equal_intro_case + (
    (
        # equal test: 1 same + 1 diff arg for each - no third arg - no error for optional third
        (
            TextNode("A node with italic and url",
                     "italic", "http://hello.world"),
            TextNode("A node with italic and url",
                     "italic", "http://hello.world")
        ),
    ),
    (
        # equal test: 1 same + 1 diff arg for each - no third arg - no error for optional third
        (
            TextNode("A node with italic and url",
                     "bold", "http://hello.world"),
            TextNode("A node with italic and url",
                     "bold", "http://hello.world")
        ),
    ),
    (
        (
            TextNode("Adventure time", "bold", "http://hello.world").text,
            'Adventure time'
        ),
    ),
    (
        (
            TextNode("Adventure time", "bold", "http://hello.world").text_type,
            'bold'
        ),
    ),
    (
        (
            TextNode("Adventure time", "bold", "http://hello.world").url,
            'http://hello.world'
        ),
    )
)
equal_cases_NOK = (
    (
        # equal test: 1 same + 1 diff arg for each - no third arg - no error for optional third
        (
            TextNode("This is a text node - diff type", "bold"),
            TextNode("This is a text node - diff type", "italic")
        ),
        False
    ),
    (
        # equal test: 1 same + 1 diff arg for each - no third arg - no error for optional third
        (
            TextNode("Blob node - diff text",
                     "italic", "http://hello.world"),
            TextNode("Plop node - diff text",
                     "italic", "http://hello.world")
        ),
        False
    ),
)

# -------------------------------- REPR CASES -------------------------------- #
repr_cases_OK = (
    (
        (
            TextNode('Node text', 'italic')
        ),
        "TextNode(Node text, italic, None)"
    ),
    (
        (
            TextNode('Node text', 'bold', 'http://helloworld.com')
        ),
        "TextNode(Node text, bold, http://helloworld.com)"
    )
)

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


if __name__ == "__main__":
    unittest.main()
