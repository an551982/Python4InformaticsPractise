total = 0
count = 0
average = 0

input = None
while True:
    input = raw_input("Enter a number:")
    if input != 'done':
        try:
            input = int(input)
            count += 1
            total += input
            average = float(total) / count
        except:
            print "Invalid input"
            continue
    else:
        print total, count, average 
        break

