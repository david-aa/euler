
import math

primesCache = {}
nPrimes = 0
aMax = 0
bMax = 0

def isPrime(n):
	if n in primesCache:
		return True
	if n == 2:
		primesCache[n] = True
		return True
	if n < 2 or n % 2 == 0:
		return False;
	max = int(math.sqrt(n));
	for i in range(3, max+1, 2):
		if n % i == 0:
			return False
	primesCache[n] = True
	return True

def checkNPrimes(a, b):
	primesTemp = 0
	n = 0
	while True:
		num = n**2 + a*n + b
		if isPrime(num):
			primesTemp += 1
		else:
			break
		n += 1
	return primesTemp

for a in range(-999, 1000):
	for b in range(-1000, 1001):
		np = checkNPrimes(a, b)
		if np > nPrimes:
			nPrimes = np
			aMax = a
			bMax = b
			print "Consecutive primes for A =", aMax, "and B =", bMax, " => ", nPrimes, "// Product A*B =", aMax*bMax

