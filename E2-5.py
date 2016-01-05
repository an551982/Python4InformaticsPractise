Celsius = raw_input("Enter a Celsius degree number: ")

try:
    Celsius = float(Celsius)
except:
    print "Invalid Celsius temperature."
    exit()
print "The Fahrenheit degree for Celsius degree", Celsius, "is", 32 + Celsius * 1.8


