def printName(first, last):
    print(first, last)

print('Last line')
printName('Bob', 'Smith')

# coding exercise - convert decimal to binary
def getBinaryRep(n, numDigits):
    '''
    Returns a binary string representation of n
    n - the number to be converted
    numDigits - how many binary digits to use
    '''
    result = ''

    while n > 0:
        digit = str(n % 2)
        result = digit + result
        n = n // 2

    # too big for the specified size
    if len(result) > numDigits:
        raise ValueError('Not enough digits')

    # too small for the specified size
    for x in range(numDigits - len(result)):
        result = '0' + result

    return result

print(getBinaryRep(250, 8))