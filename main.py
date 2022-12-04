coordinating_functions = ['for', 'and', 'nor', 'but', 'or', 'yet', 'so']

def check_words(word):
    tracker ={}
    if word in coordinating_functions:
        if word not in tracker.keys():
            tracker[word]=1
        else:
            tracker[word]={tracker[word]+1}
    for x, y in tracker.items():
        print(f"{x}:{y}")


with open('test.txt', 'r') as f:
    for line in f:
        for word in line.split():
            check_words(word)