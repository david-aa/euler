#!/usr/bin/env python3

divisors = range(1, 20);
test = divisors[-1]
control = True
while control:
    divisible = True
    for d in divisors:
        if test % d != 0:
            divisible = False
            break

    if divisible:
        control = False
    else:
        test += 1

print (test)
