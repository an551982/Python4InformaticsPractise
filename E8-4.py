inp = raw_input("Enter file: ")
fl = open(inp)
wordsList = list()
for line in fl:
    words = line.split()
    for wd in words:
        if wd in wordsList: continue
        wordsList.append(wd)
    wordsList.sort()

print wordsList

