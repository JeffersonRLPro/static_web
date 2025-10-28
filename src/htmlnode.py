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
                string.append(f'{key}={self.props[key].strip()}')
            return " ".join(string)
        else:
            return None
    
    def __repr__(self):
        return f"""
        tag: {self.tag},
        value: {self.value},
        children: {self.children},
        props: {self.props}
        """