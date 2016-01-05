def computegrade(score):
    if score < 0 or score >= 1:
        return "Bad score"
    elif score > 0.9:
        return "A"
    elif score > 0.8:
        return "B"
    elif score > 0.7:
        return "C"
    elif score > 0.6:
        return "D"
    else:
        return "F"

print "Score\tGrade"
print "> 0.9\tA"
print "> 0.8\tB"
print "> 0.7\tC"
print "> 0.6\tD"
print "<= 0.6\tF"

print "\nProgram Execution:"

while True:
    sc = raw_input("Enter score:")
    if sc.lower() != "quit":
        try:
            sc = float(sc)
        except:
            print "Bad score"
            continue
        print computegrade(sc)
    else:
        break
