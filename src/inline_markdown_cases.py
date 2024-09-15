from inline_markdown import *

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
)

split_nodes_delimiter_error_cases = (
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
