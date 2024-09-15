from textnode import *

# ---------------------------------------------------------------------------- #
#                            SPLITTER [ delimiter ]                            #
# ---------------------------------------------------------------------------- #
pattern_img = r'!\[\w.*?\]\(https?://\w.*?\)'
pattern_link = r'\[\w.*?\]\(https?://\w.*?\)'
pattern_link2 = r"\[\w.+?\]\(\w.+?\)"
media_pattern = rf"{pattern_img}|{pattern_link}"


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
                element.split('](')
            ))
        for element in markdown_elements
    ]
    return markdown_elements_details


def extract_markdown_images(string):
    return extract_markdown_element(pattern_img, string)


def extract_markdown_links(string):
    return extract_markdown_element(pattern_link2, string)


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


def assign_media_text_node(string):
    link = extract_markdown_links(string)
    image = extract_markdown_images(string)

    if image:
        return TextNode(image[0][0], 'image', image[0][1])
    elif link:
        return TextNode(link[0][0], 'link', link[0][1])
    return TextNode(string, 'text')


def split_images_and_links(original_nodes):

    # find where to split
    for node in original_nodes:
        text = node.text

        # media kind list - matches both link and image
        medias = re.findall(media_pattern, text)

        # raw text content list
        other_texts = re.split(media_pattern, text)

        # merged list
        both = [*filter(lambda x: len(x), medias + other_texts)]

        # retrieving term string and their indexes - in order later to sort them
        final = []
        for i in range(len(both)):
            final.append(
                text.index(both[i])
            )

        # interface right index for each value
        interfaced = [*zip(final, both)]

        # sort interfaced text tuple
        correct_texts_order_tuples = sorted(interfaced)

        # create new ordered text
        correct_texts_order = [*map(
            lambda tuple: tuple[1],
            correct_texts_order_tuples
        )]

        text_nodes = [*map(
            assign_media_text_node,
            correct_texts_order
        )]

    return text_nodes
