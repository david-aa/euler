


def checkSumDigits(number, power):
	_sum = 0
	for digit in str(number):
		_sum += (int(digit))**power
	return _sum == number

final_sum = 0
# Narcisist number: http://mathworld.wolfram.com/NarcissisticNumber.html
for a in range(2, 10**6):
	if checkSumDigits(a, 5):
		print a
		final_sum += a
print final_sum