#!/usr/bin/env python
import sys
import pprint
# Euler #31

coins = (1, 2, 5, 10, 20, 50, 100, 200)
amount = int(sys.argv[1])
print "Trying to parse", amount

def dissambleAmount(a):
	ret = []
	for c in coins:
		if c > a:
			break
		ret2 = []
		ret2.append(c)
		ret2.append(dissambleAmount(a - c))
		ret.append(ret2)
	return ret

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(dissambleAmount(amount))