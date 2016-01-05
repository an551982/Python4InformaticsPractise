def count(strg, lttr):
    counter = 0
    for letter in strg:
        if letter == lttr:
            counter += 1
    return counter

word = 'banana'
print count(word, 'a')

