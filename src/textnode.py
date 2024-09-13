class TextNode():
    def __init__(self, text, text_type: 'bold' or 'italic', url=None):
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
