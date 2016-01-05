def cal_rates(hrs, rt):
    if hrs < 0:
        print "Wrong Input."
        exit()
    elif hrs <= 40:
        return rt * hrs
    else:
        return 40 * rt + (hrs - 40) * rt * 1.5

try:
    hours = float(raw_input("Enter Hours:"))
except:
    print "Error, please enter numeric input."
    exit()

try:
    rate = float(raw_input("Enter Rate:"))
except:
    print "Error, please enter numeric input."
    exit()

print "Pay:", cal_rates(hours, rate)



