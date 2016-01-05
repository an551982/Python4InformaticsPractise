


#################
#   Chapter4
#################

###Module: random
import random

#random()
for i in range(10):
   x = random.random()
   print x


#randint(low,high)
random.randint(1,10)
random.randint(1,10)


#choice(list)
t = range(10)
random.choice(t)


###Module: math
import math

math.log10(1)   #0.0
math.sin(30)   #radian as the argument. radians = degrees * 2 * math.pi /360.0
radians = 30 * 2 * math.pi / 360
math.sin(radians)   #0.49999999999999994
math.sqrt(2)   #1.4142135623730951

###Defining functions
def print_some():
   print 'print something.'
   
type(print_some)   #<type 'function'>

#repr(object)
string = '1 2\t 3\n 4'
print string
print repr(string)

test = {'a':1, 'b':2, 'c':3}
print repr(test)


#format operator
#https://docs.python.org/2/library/stdtypes.html#string-formatting.
print 'In %d years I have spotted %g %s.' % (3, 1.5, 'camels')


