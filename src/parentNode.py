
from htmlnode import HTMLNode
from leafnode import LeafNode


class ParentNode(HTMLNode):
    def __init__(self, a, children: [str] = []):
        super().__init__(a, None, children, None)

    def to_html(self):
        if not self.tag:
            raise ValueError('ParentNode must have a tag')
        if not self.children:
            raise ValueError('ParentNode must have children')

        children = list(
            map(
                lambda x: x.to_html(),
                self.children
            )
        )
        return f"<{self.tag}>{''.join(children)}</{self.tag}>"
