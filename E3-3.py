
while True:
    try:
        score = float(raw_input("Enter score:"))
    except:
        print "Bad score"
        continue

    if ( score < 0 or score > 1.0 ) and score != -1:
        print "Bad score"
    elif score >= 0.9:
        print "A"
    elif score >= 0.8:
        print "B"
    elif score >= 0.7:
        print "C"
    elif score >= 0.6:
        print "D"
    elif score < 0.6 and score >= 0:
        print "F"
    elif score == -1:
        exit() 








