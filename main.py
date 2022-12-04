from Document import Document

load_file = r'C:\Users\jakem\Desktop\Gramma-Pro\test.txt'
coordinating_functions = ['for', 'and', 'nor', 'but', 'or', 'yet', 'so']
tracker ={}

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
    
    

with open(load_file, 'r') as f:
    for line in f:
        for word in line.split():
            check_words(word)

display_results(tracker)

doc = Document(load_file)
print(doc.read_file())