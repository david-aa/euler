

def get_divisors(num):
	divisors = []
	for x in range(1, num/2 + 1):
		if num % x == 0:
			divisors.append(x)
	return divisors

def find_amicable_for(num):
	sum_divs = sum(get_divisors(num))
	if sum(get_divisors(sum_divs)) == num and sum_divs != num:
		return sum_divs
	return False


if __name__ == '__main__':
	print get_divisors(28)
	amicables = []
	for x in range(1, 10000):
		a = find_amicable_for(x)
		if a is not False:
			amicables.append(a)

	print amicables
	print sum(amicables)		