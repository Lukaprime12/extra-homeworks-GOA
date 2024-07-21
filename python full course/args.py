def sumification(*stuff):
    sum = 0
    stuff = list(stuff)
    stuff[0]=0
    for i in stuff:
        sum += i
    return sum


print(sumification(1,2,3,4,5,6,7,8))