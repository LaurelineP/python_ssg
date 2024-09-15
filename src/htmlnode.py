
from class_helpers import get_class_repr


class HTMLNode():
    def __init__(self,
                 tag: str = None,
                 value: str = None,
                 children: [str] = None,
                 props: dict = None
                 ):

        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if not self.props == None:
            attributes_str = []
            for prop in self.props:
                attributes_str.append(f'{prop}="{self.props[prop]}"')
            return f" {' '.join(attributes_str)}"
        return ''

    def __repr__(self):
        class_repr = get_class_repr(self, 'HTMLNode')
        return class_repr


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
