from htmlnode import *

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


leaf_node_representation_equal_cases = (
    (
        LeafNode('a', 'the link', {'href': 'https://hello.world'}),
        f"HTMLNode(a, the link, None, {str({ 'href': 'https://hello.world' })})"
    ),
)

leafNode_to_html_equal_cases = (
    (
        LeafNode('a', 'the link 2', {'href': 'https://hello.world'}).to_html(),
        f'<a href="https://hello.world">the link 2</a>'
    ),
    (
        LeafNode(None, 'the link 3').to_html(),
        f'the link 3'
    ),
)


parentNode_to_html_cases = (
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
