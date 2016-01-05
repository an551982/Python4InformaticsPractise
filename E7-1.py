def shout(fname):
    for line in fname:
        print line.upper().rstrip()

input = raw_input('Enter a file name: ')
try:
    filename = open(input)
except:
    print 'The file with the name "%s" cannot be opened' % input 
    exit()

shout(filename)


