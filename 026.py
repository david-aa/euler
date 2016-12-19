
from decimal import Decimal, getcontext

getcontext().prec = 40

def Div(D, d):
	return (D/d, D%d)

def GetPeriod(d):
	period = []
	remainders = []
	index = 0
	c, r = Div(1, d)
	if r == 0:
		return []
	if c != 0:
		period.append(c)
	while True:
		D = 10*r
		c, r = Div(D, d)
		if r == 0:
			return []
		period.append(c)
		if r in remainders:  
			return period[period.index(c):index]
		index += 1
		remainders.append(r)

	return period


longestList = []
longestInt = 1
for a in range(1, 1000):
	period = GetPeriod(a)
	if len(period) > len(longestList):
		longestList = period
		longestInt = a

print "Longest period for ", longestInt, " => ", longestList, " (len: ", len(longestList), ")"



