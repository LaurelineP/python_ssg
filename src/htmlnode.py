
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
                attributes_str.append(f"{prop}={self.props[prop]}")
            return f" {' '.join(attributes_str)}"
        return ''

    def __repr__(self):
        class_repr = get_class_repr(self, 'HTMLNode')
        return class_repr
