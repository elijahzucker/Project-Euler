def collatize(n):
    c = 1                   #c is the count of terms in the string
    while(n > 1):           #runs oddOrEven until it produces 1
        n = oddOrEven(n)
        c += 1

    return c

def oddOrEven(n):           #piecewise function that applies on operation if n is odd or even
    if( (n % 2) == 0):
        n = n/2
    else:
        n = 3 * n + 1
    return n

def runProb(x):             #x here is the max starting number
    i = 0
    c = 0                   #tracks longest count
    cStart = 0              #tracks the starting num of longest count
    while(i <= x):
        b = collatize(i)
        if(b > c):
            c = b
            cStart = i
        i += 1
    print(cStart)
