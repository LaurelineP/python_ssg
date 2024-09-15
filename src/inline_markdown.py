from textnode import *

# ---------------------------------------------------------------------------- #
#                            SPLITTER [ delimiter ]                            #
# ---------------------------------------------------------------------------- #
pattern_img = r'!\[\w.*?\]\(https?://\w.*?\)'
pattern_link = r'\[\w.*?\]\(https?://\w.*?\)'
pattern_link2 = r"\[\w.+?\]\(\w.+?\)"


def split_nodes_delimiter(original_nodes: [TextNode], delimiter: str, text_type: str = None):
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


def split_nodes_link(original_nodes):
    # find where to split
    for node in original_nodes:
        text = node.text
        splitted_text = [*map(
            lambda s: f"[{s}" if '(' in s and ')' in s and ']' in s else s,
            text.split('[')
        )]
        # splitted_text = re.split(pattern_link, text)
        # parsed = [*map(
        #     lambda s: TextNode(s, TextType.TEXT)
        #     if not (s.startswith('[') and s.endswith(')'))
        #     # else TextNode(s, TextType.LINK),
        #     else TextNode(s, TextType.LINK),
        #     splitted_text
        # )]
        print('\n🔥splitted_text', splitted_text)
        # print('\n🔥parsed', parsed)


# test = re.findall(r"\[\w.+?\]\(\w.+?\)$",
#                   "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
test = re.split(r"\[\w.+?\]\(\w.+?\)",
                "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")

# print('🔥 other than link:', test)
# node = TextNode(
#     "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
#     TextType.TEXT,
# )
# new_nodes = split_nodes_link([node])
# # [
# #     TextNode("This is text with a link ", text_type_text),
# #     TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
# #     TextNode(" and ", text_type_text),
# #     TextNode(
# #         "to youtube", text_type_link, "https://www.youtube.com/@bootdotdev"
# #     ),
# # ]


# ---------------------------------------------------------------------------- #
#                        EXTRACTORS [ LINKS AND IMAGE ]                        #
# ---------------------------------------------------------------------------- #


def extract_markdown_element(pattern, string):
    pattern_removable = r"!|\[|\]\(|\)"

    # all markdown string
    markdown_elements = re.findall(pattern, string)

    # markdowns image text infos - without markdown syntax
    markdown_elements_details = [
        tuple(
            map(
                lambda s: re.sub(pattern_removable, '', s),
                image.split('](')
            ))
        for image in markdown_elements
    ]
    return markdown_elements_details


def extract_markdown_images(string):
    return extract_markdown_element(pattern_img, string)


def extract_markdown_links(string):
    return extract_markdown_element(pattern_link2, string)
