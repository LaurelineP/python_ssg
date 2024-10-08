import re
from enum import Enum

from htmlnode import LeafNode


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
