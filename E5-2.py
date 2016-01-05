maxNum = None
minNum = None

input = None
while True:
    input = raw_input("Enter a number:")
    if input != 'done':
        try:
            input = int(input)
            if maxNum == None or maxNum < input:
                maxNum = input
            if minNum == None or minNum > input:
                minNum = input 
        except:
            print "Invalid input"
            continue
    else:
        print maxNum, minNum 
        break

