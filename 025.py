
fib_numbers_cache = {}

def fib(num):
	if num in fib_numbers_cache:
		return fib_numbers_cache[num]
	if num <= 2:
		fibNum = 1
	else:
		fibNum = fib(num - 1) + fib(num - 2)
	fib_numbers_cache[num] = fibNum
	return fibNum

n = 1
n_digits = 1000
fib_num_max = 10**(n_digits - 1) - 1
while True:
	fn = fib(n)
	if fn > fib_num_max:
		print "END: ", n, "=>", fn
		break
	n += 1

