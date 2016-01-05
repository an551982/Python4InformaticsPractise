numList = []
while True:
    inp = raw_input("Enter a number: ")
    if inp == "done": break
    numList.append(float(inp))
    
print "Maximum:", max(numList)
print "Minimum:", min(numList)


