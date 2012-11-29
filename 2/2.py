def fib(n):
	"""
	>>> [fib(n) for n in range(5)]
	[1, 2, 3, 5, 8]
	"""
	if n == 0:
		return 1
	elif n == 1:
		return 2
	else:
		return fib(n-1) + fib(n-2)

def sum_of_even_fib_v1(maxFibValue):
	"""
	>>> [sum_of_even_fib_v1(maxFibValue) for maxFibValue in range(10)]
	[0, 0, 2, 2, 2, 2, 2, 2, 10, 10]
	"""
	n = 0
	total = 0
	while True:
		fibValue = fib(n)
		if fibValue > maxFibValue:
			return total
		if fibValue % 2 == 0:
			total += fibValue
		n += 1

def sum_of_even_fib_v2(maxFibValue):
	"""
	>>> [sum_of_even_fib_v2(maxFibValue) for maxFibValue in range(10)]
	[0, 0, 2, 2, 2, 2, 2, 2, 10, 10]
	>>> sum_of_even_fib_v2(4000000)
	4613732
	"""
	a = 1
	b = 1
	sum = 0
	while b <= maxFibValue:
		if b % 2 == 0:
			sum += b
		newB = a + b
		a = b
		b = newB
	return sum

if __name__ == "__main__":
	import doctest
	doctest.testmod()

	max = 4000000
	print("The sum of the even-valued terms in the Fibonacci sequence whose values do not exceed {:,} is:".format(max))
	#print("Method 1: {}".format(sum_of_even_fib_v1(max)))
	print("Method 2: {}".format(sum_of_even_fib_v2(max)))
