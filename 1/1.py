def is_multiple(n):
	"""
	>>> is_multiple(0)
	True
	>>> is_multiple(1)
	False
	>>> is_multiple(2)
	False
	>>> is_multiple(3)
	True
	>>> is_multiple(5)
	True
	>>> is_multiple(11)
	False
	>>> is_multiple(30)
	True
	>>> is_multiple(55)
	True
	>>> is_multiple(66)
	True
	"""
	return ((n % 3) == 0) or ((n % 5) == 0)

def sum_of_multiples_v1(limit):
	"""Return the sum of all multiples of 3 or 5 below limit.

	>>> sum_of_multiples_v1(10)
	23
	>>> sum_of_multiples_v1(1000)
	233168
	"""
	total = 0
	for n in range(limit):
		if is_multiple(n):
			total += n
	return total

def sum_of_multiples_v2(limit):
	"""Return the sum of all multiples of 3 or 5 below limit.

	>>> sum_of_multiples_v2(10)
	23
	>>> sum_of_multiples_v2(1000)
	233168
	"""
	multiples = [n for n in range(limit) if is_multiple(n)]
	return sum(multiples)

def sum_of_numbers_divisible_by(divisor, limit):
	"""
	>>> sum_of_numbers_divisible_by(3, 10)
	18.0
	"""
	p = (limit - 1) // divisor
	# uses the fact that (1 + 2 + ... + n) == (n * (n+1) / 2)
	return divisor * p * (p + 1) / 2

def sum_of_multiples_v3(limit):
	"""Return the sum of all multiples of 3 or 5 below limit.

	>>> sum_of_multiples_v3(10)
	23.0
	>>> sum_of_multiples_v3(1000)
	233168.0
	"""
	return sum_of_numbers_divisible_by(3, limit) \
		+ sum_of_numbers_divisible_by(5, limit) \
		- sum_of_numbers_divisible_by(15, limit)

if __name__ == "__main__":
	import doctest
	doctest.testmod()

	limit = 1000
	print("The sum of all multiples of 3 or 5 below {} is:".format(limit))
	print("Method 1: {}".format(sum_of_multiples_v1(limit)))
	print("Method 2: {}".format(sum_of_multiples_v2(limit)))
	print("Method 3: {}".format(sum_of_multiples_v3(limit)))