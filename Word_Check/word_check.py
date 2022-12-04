class WordCheck:
    
    def __init__(self, file:str) -> None:
        self.file = file
        
    def read_file(self):
        with open(self.file, 'r') as f:
            return f.read()
        
    def check_words(word):
        if word in coordinating_functions:
            if word not in tracker.keys():
                tracker[word]=1
            else:
                tracker[word]=tracker[word]+1


    def display_results(results: dict[str:int]):
        total: int = 0
        for x, y  in results.items():
            total += y
            print(f"conjunction found: '{x}'\ncount: {y}")
        print(f"Total Co-ordinating Conjunction found: {total}")