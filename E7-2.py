def count_confidence(fn):
    totalConfidence = 0   
    count = 0
    for line in fn:
        if not line.startswith('X-DSPAM-Confidence:'):
            continue
        count += 1
        totalConfidence += float(line.split(':')[1])
    return totalConfidence / count

input = raw_input('Enter the file name: ')
try:
    file = open(input)
except:
    print 'file: %s cannot be opened.' % input
    exit()

print 'Average spam confidence:', count_confidence(file)

