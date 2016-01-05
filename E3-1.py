def cal_rates(hrs, rt):
    if hrs < 0:
        print "Wrong Input."
        exit()
    elif hrs <= 40:
        return rt * hrs
    else:
        return 40 * rt + (hrs - 40) * rt * 1.5


hours = raw_input("Enter Hours:")
rate = raw_input("Enter Rate:")
try:
    hours = float(hours)
    rate = float(rate)
except:
    print "The hours or rate you input is invalid."
    exit()

print "Pay:", cal_rates(hours, rate)



