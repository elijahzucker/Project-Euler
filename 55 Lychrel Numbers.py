def lycrize(x):
    i = 0                           #i is a var to contain the number of checks preformed
    while(i < 50):          
        y = x + reverseNum(x)       #adds x to its reverse then checks to see if its a palindrome
        if( palindromeCheck(y) ):
            return False
        x = y                       #as long as its not a palindrome sets new x to the calculated y
        i += 1
    return True

def reverseNum(x):                  #simple function to reverse order of int
    r = 0
    while(x > 0):
        y = x % 10
        r = (r * 10) + y
        x = x // 10
    return r

def palindromeCheck(x):             #converts to string then compares itself to its reverse
    s = str(x)
    if (s == s[::-1]):
        return True
    else:
        return False

def lychrelsInRange(x):
    c = 0                           #runs lycrize() x times and then prints successes
    for i in range(x):
        if( lycrize(i) ):
            c += 1
    print(c)
