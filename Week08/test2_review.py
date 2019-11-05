# Practice Test #2, Question #4
import re

price_re = re.compile('\$[0-9]+(\.[0-9]{2})?')
price_match = price_re.search('I bought this for $99.99 in July..')
if price_match:
    print('Found a price:', price_match.group())
else:
    print('No prices found')

# Practice Test #2, Question #2
def isPalindrome(string):
    if len(string) <= 1:
        return True 
    
    if string[0] != string[-1]:
        return False
    
    return isPalindrome(string[1:-1])


palindrome1 = 'ablewasiereisawelba'
palindrome2 = 'racecar'
print('is', palindrome1, 'a palindrome?', isPalindrome(palindrome1))
print('is', palindrome2, 'a palindrome?', isPalindrome(palindrome2))

# Sample Problems (Test #2), Question #4 (reverse)

def reverse(string):
    if len(string) <= 1:
        return string 
    
    first = string[0]
    rest = string[1:]
    return reverse(rest) + first

print(reverse('abcd'))

def reverse2(string):
    result = ''
    for c in string:
        result = c + result
    return result 
print(reverse2('abcd'))
