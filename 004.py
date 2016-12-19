#!/usr/bin/env python3

def isPalindromic(arg):
    arg = str(arg)
    cut = int(len(arg)/2)
    (first, last) = (arg[:cut], arg[cut:][::-1])
    if (len(last) == len(first) + 1):
        last = last[:-1]
    return first == last
    
biggest = 0    
for x in range(100, 1000):
    for y in range(100, 1000):
        num = x * y
        if isPalindromic(num) and num > biggest:
            biggest = num
            
print (biggest)