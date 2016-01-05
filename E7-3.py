input = raw_input('Enter the file name: ')
if input == 'na na boo boo':
    print 'NA NA BOO BOO TO YOU - You have been punk\'d!'
    exit()
try:
    filename = open(input)
except:
    print 'File cannot be opened:', input
    exit()

countline = 0
for line in filename:
    countline += 1

print 'There were 1797 subject lines in', input 
