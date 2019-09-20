value = 17
print('Value:', value, sep='', end='')
print('Next line')

for x in range(9999999999999999):
    if x**2 == 100:      
        print(x)
        break

# infinite loop
#x = 1
#while True:
#    x += 1
#    print('Hello')

x = 81.0
epsilon = 0.0000000000000001
low = 0
high = x
guess = (high + low) / 2.0
while abs(guess**2 - x) >= epsilon:
    if guess**2 < x:
        low = guess 
    else:
        high = guess 
    guess = (high + low) / 2.0

print('Guess:', guess)

import math
x = 2.0
maxN = 100
sum = 1.0
for n in range(1, maxN):
    term = x**n / math.factorial(n)
    sum += term 
print('e**', x, '=', sum)