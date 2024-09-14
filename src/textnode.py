import re
from enum import Enum

from leafnode import LeafNode


class TextNode():

    ''' Intermediary between text node Markdown x HTML node '''

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return all([
            self.__dict__[property] == other.__dict__[property]
            for property in self.__dict__
        ])

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


type_delimiters = {
    'TEXT': '',
    'BOLD': '**',
    'ITALIC': '*',
    'CODE': '`',
    'LINK': '',
    'IMAGE': ''

}
TextType = Enum('TextType', list(type_delimiters.keys()))


def text_node_to_html_node(text_node_entity: TextNode):
    text_type = text_node_entity.text_type.upper()
    value = text_node_entity.text
    url = text_node_entity.url

    if not TextType[text_type]:
        raise Exception('Invalid text node type')
    else:
        # ------------------------------- PYTHON >3.10 ------------------------------- #
        # match TextType[text_type]:
        #     case TextType.TEXT:
        #         return LeafNode(None, value).to_html()
        #     case TextType.BOLD:
        #         return LeafNode('b', value).to_html()
        #     case TextType.ITALIC:
        #         return LeafNode('i', value).to_html()
        #     case TextType.CODE:
        #         return LeafNode('code', value).to_html()
        #     case TextType.LINK:
        #         # return LeafNode('a', value,  url).to_html()
        #         return LeafNode('a', value, {"href": url}).to_html()
        #     case TextType.IMAGE:
        #         return LeafNode('img', value, {"src": url, "alt": value}).to_html()
        #     case _:
        #         return 'NOT PROCESSED'

        # ------------------------------- PYTHON <3.10 ------------------------------- #
        if TextType[text_type] == TextType.TEXT:
            return LeafNode(None, value).to_html()
        elif TextType[text_type] == TextType.BOLD:
            return LeafNode('b', value).to_html()
        elif TextType[text_type] == TextType.ITALIC:
            return LeafNode('i', value).to_html()
        elif TextType[text_type] == TextType.CODE:
            return LeafNode('code', value).to_html()
        elif TextType[text_type] == TextType.LINK:
            return LeafNode('a', value, {"href": url}).to_html()
        elif TextType[text_type] == TextType.IMAGE:
            return LeafNode('img', value, {"src": url, "alt": value}).to_html()


def split_nodes_delimiter(original_nodes: [TextNode], delimiter: str, text_type: str = None):
    # print('😱', not delimiter.upper() in type_delimiters.keys())
    # if delimiter and not delimiter.upper() in type_delimiters.values():
    #     raise Exception('Invalid Markdown syntax')

    # for each node - string splitted
    texts = [*map(
        lambda node: node.text.split(delimiter),
        original_nodes
    )]

    # finds text type accorded to delimiter
    delimited_type = text_type or None
    if not delimited_type:
        for delimiter_details in type_delimiters.items():
            if delimiter in delimiter_details:
                delimited_type = delimiter_details[0].lower()
                break

    has_closing_delimiter = all(map(lambda x: x.text.count(delimiter) %
                                    2 == 0, original_nodes))
    is_known_delimiter = delimiter in type_delimiters.values()

    is_know_text_type = delimited_type.upper() in type_delimiters.keys()
    if not is_known_delimiter or not has_closing_delimiter:
        raise Exception('Invalid Markdown syntax')

    if not is_know_text_type:
        raise Exception('Invalid text type for Markdown')

    # create adjusted TextNode for each splitted strings
    new_node_parts = []
    for text_parts in texts:
        for text_part in text_parts:
            _type = 'text' \
                if text_part.startswith(' ') or text_part.endswith(' ') \
                else delimited_type
            new_node_parts.append(TextNode(text_part, _type))

    return new_node_parts


def extract_markdown_images(string):
    # pattern = r'!\[\w+\]\(https?:\/\/\w*\/+\)`'
    pattern = r'!\[\w.*?\]\(https?://\w.*?\)'

    markdown_links = re.findall(pattern, string)
    markdown_links_details = [
        link.replace(
            r"[!|\[|\(|\)|\]]", '') for link in markdown_links]
    print('🔥 pattern:', pattern)
    print('🔥 markdown_links:', markdown_links)
    print('🔥 markdown_links_details:', markdown_links_details)


text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
print(extract_markdown_images(text))
# [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
