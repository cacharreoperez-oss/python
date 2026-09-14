class File:

    def __init__(self,path:str):
        self.path =path
        self.content = []
        
    def add_contentb(self,content:list):
        self.content=content
    @property
    def size(self):
        pass

    @property
    def info(self):
        pass

