from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict = None):
        super().__init__(
            tag,
            value=value,
            children=None,
            props=props
        )

    def to_html(self):
        if not self.value:
            raise ValueError('LeafNode must have a value')

        if not self.tag:
            return self.value

        attributes = super().props_to_html()
        start_tag = f"<{self.tag}{attributes}>" if attributes else f"<{self.tag}>"
        return f"{start_tag}{self.value}</{self.tag}>"
