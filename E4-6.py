def computepay(hours, rate):
    if hours > 40:
        return 40 * rate + (hours - 40) * 1.5 * rate
    else:
        return hours * rate

while True:
    hrs = raw_input("Enter Hours:")
    rt = raw_input("Enter Hours:")
    try:
        hrs = float(hrs)
        rt = float(rt)
        break
    except:
        print "Bad input of hours or rate.\nInput again."
        continue

print "Pay:", computepay(hrs, rt)



