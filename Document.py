class Document:
    
    def __init__(self, file:str) -> None:
        self.file = file
        
    def read_file(self):
        with open(self.file, 'r') as f:
            return f.read()