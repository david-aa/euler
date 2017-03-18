numbers = []
for a in range(2, 101):
	for b in range(2, 101):
		n = a**b
		if not n in numbers:
			numbers.append(n)

numbers.sort() 
print len(numbers)

