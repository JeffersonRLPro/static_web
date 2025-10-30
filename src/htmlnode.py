class HTMLNode:
    def __init__(self, tag:str=None, value:str=None, children:list[object]=None, props:dict=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props:
            string = []
            for key in self.props.keys():
                string.append(f'{key}="{str(self.props[key]).strip()}"')
            return " ".join(string)
        else:
            return None
    
    def __repr__(self):
        return f"""HTMLNode(
        tag: {self.tag},
        value: {self.value},
        children: {self.children},
        props: {self.props}
        )
        """
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props : dict=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        # if the value is None raise an exception
        if not self.value:
            raise ValueError(f"Error: The value of a LeafNode cannot be None: {self.value}")
        if not self.tag:
            return self.value
        if not self.props:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        else:
            return f'<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self, tag, children : list[object], props : dict=None):
        super().__init__(tag, None, children, props)
        # check all varibales to ensure they are all correct
        if self.children is None:
            raise ValueError("Error: The children list cannot be None")
        if not isinstance(self.children, list):
            raise ValueError("Error: Children must be a list")
        if len(self.children) == 0:
            raise ValueError("Error: The children list cannot be empty")
        if not all(isinstance(node, HTMLNode) for node in self.children):
            raise ValueError(f"Error: All elements in the children list must be HTMLNode objects: {self.children}")
    
    def to_html(self):
        if not self.tag:
            raise ValueError(f"Error: The tag of a ParentNode cannot be None: {self.tag}")
        string = ""
        for node in self.children:
            string += node.to_html()
        if not self.props:
            return f"<{self.tag}>{string}</{self.tag}>"
        else:
            return f"<{self.tag} {self.props_to_html()}>{string}</{self.tag}>"