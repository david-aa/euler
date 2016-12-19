
def fact(n):
	if n <= 1:
		return 1
	else:
		return n * fact(n -1)

s = 0
for a in str(fact(100)):
	s += int(a)
print s