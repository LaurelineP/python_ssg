import unittest

# from helpers import text_node_to_html_node
from test_helpers import *
from textnode import *

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


# -------------------------------- REPR CASES -------------------------------- #
textnode_to_html = (
    (
        text_node_to_html_node(TextNode('regular text', 'text')),
        'regular text'
    ),
    (
        text_node_to_html_node(TextNode('bold text', 'bold')),
        '<b>bold text</b>'
    ),
    (
        text_node_to_html_node(TextNode('italic text', 'italic')),
        '<i>italic text</i>'
    ),
    (
        text_node_to_html_node(TextNode('code text', 'code')),
        '<code>code text</code>'
    ),
    (
        text_node_to_html_node(
            TextNode('link text', 'link', "https://links.co")),
        '<a href="https://links.co">link text</a>'
    ),

)

log_test('TestTextNodeToHTML')


class TestTextNodeToHTML(unittest.TestCase):

    @log_test_with(len(textnode_to_html))
    def test_representation(self):
        assertEqual(textnode_to_html)


split_nodes_delimiter_cases = (
    # testing absent optional text_type ( to changed to )
    (
        split_nodes_delimiter(
            [TextNode("This is text with a `code block` word",  'text')],
            "`"
        ),
        '[TextNode(This is text with a , text, None), TextNode(code block, code, None), TextNode( word, text, None)]'
    ),

    # testing absent optional text_type ( to changed to )
    (
        split_nodes_delimiter(
            [TextNode("This is text with a `code block` word",  'text')],
            "`", 'code'
        ),
        '[TextNode(This is text with a , text, None), TextNode(code block, code, None), TextNode( word, text, None)]'
    ),
    # testing multiple nodes
    (
        split_nodes_delimiter(
            [
                TextNode("This is text with a `code block` word",  'text'),
                TextNode("This is text with a `code block` word",  'text'),
                TextNode("This is text with a `code block` word",  'text'),
            ],
            "`", 'code'
        ),
        '[TextNode(This is text with a , text, None), TextNode(code block, code, None), TextNode( word, text, None), TextNode(This is text with a , text, None), TextNode(code block, code, None), TextNode( word, text, None), TextNode(This is text with a , text, None), TextNode(code block, code, None), TextNode( word, text, None)]'
    ),
    # Ensures all nodes are at the same level
    (
        len(split_nodes_delimiter(
            [
                TextNode("This is text with a `code block` word",  'text'),
                TextNode("This is text with a `code block` word",  'text'),
                TextNode("This is text with a `code block` word",  'text'),
            ],
            "`", 'code'
        )),
        '9'
    ),
    # # override non conventionned delimiter by another text type
    (
        split_nodes_delimiter(
            [TextNode("This is text with a `code block` word", 'text')],
            "`", 'italic'
        ),
        '[TextNode(This is text with a , text, None), TextNode(code block, italic, None), TextNode( word, text, None)]'
    ),
    (
        split_nodes_delimiter(
            [TextNode("This is text with a `code block` word", 'text')],
            "`", 'italic'
        ),
        '[TextNode(This is text with a , text, None), TextNode(code block, italic, None), TextNode( word, text, None)]'
    ),
)

split_nodes_delimiter_error_cases = (
    # tests incorrect delimiter
    (
        (
            # caller
            split_nodes_delimiter,

            # args
            [TextNode(
                "This should be an `error text` word",
                'text'
            )],
            "+",
            'italic'
        ),
        # expected type of raised error
        Exception
    ),
    (
        (
            # caller
            split_nodes_delimiter,

            # args
            [TextNode(
                "This should be an `error text` word",
                'text'
            )],
            "`",
            'blob'
        ),
        # expected type of raised error
        Exception
    )
)

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


if __name__ == "__main__":
    unittest.main()
