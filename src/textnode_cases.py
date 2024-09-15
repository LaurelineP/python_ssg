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


# ---------------------------------------------------------------------------- #
#                         EXTRACT MARKDOWN IMAGES CASES                        #
# ---------------------------------------------------------------------------- #

# text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
# print(extract_markdown_images(text))
# # [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

extract_md_images_cases = (
    (
        extract_markdown_images(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        ),
        [("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
         ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

    ),
    (
        extract_markdown_images(
            "one image ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        ),
        [("rick roll", "https://i.imgur.com/aKaOqIh.gif")]

    ),
    (
        extract_markdown_links(
            "no image in here"
        ),
        []
    ),
)

extract_md_links_cases = (
    (
        extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        ),
        [("to boot dev", "https://www.boot.dev"),
         ("to youtube", "https://www.youtube.com/@bootdotdev")]

    ),
    (
        extract_markdown_links(
            "one link [to boot dev](https://www.boot.dev)"
        ),
        [("to boot dev", "https://www.boot.dev")]

    ),
    (
        extract_markdown_links(
            "no link in here"
        ),
        []
    ),
)
