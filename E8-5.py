inp = raw_input("Enter a file name: ")

fl = open(inp)

fromLnCnt = 0

for line in fl:
    if not line.startswith("From "): continue
    print line.split()[1]
    fromLnCnt += 1

print "There were %d lines in the file with From as the first word" % fromLnCnt


