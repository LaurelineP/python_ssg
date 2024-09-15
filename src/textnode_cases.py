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
