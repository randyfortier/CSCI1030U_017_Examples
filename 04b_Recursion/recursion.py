def repeatNTimes(n, message):
    if n < 1:
        return 
    
    print('repeatNTimes', n, 'before recursion:')
    repeatNTimes(n - 1, message)
    #print('repeatNTimes', n, 'after recursion:')

repeatNTimes(10, 'Hello')

def fib(n):
    if n == 0 or n == 1:
        return n
    
    return fib(n - 1) + fib(n - 2)

print('fib(4) =', fib(4))
print('fib(6) =', fib(6))
#print('fib(50) =', fib(50))

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return factorial(n - 1) * n

def ftoc(f):
    return (f - 32) * 5 / 9

fTemps = [10, 20, 30, 40, 50]
cTemps = list(map(ftoc, fTemps))
print(cTemps)

cTemps2 = list(map(lambda f: (f - 32) * 5 / 9, fTemps))
print(cTemps2)

