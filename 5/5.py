if __name__ == "__main__":
	import sys
	sys.path.insert(0, '..')
from Common import Prime

from collections import Counter

def product(list):
	"""
	>>> product([2, 3, 4])
	24
	>>> product([])
	1
	"""
	p = 1
	for n in list:
		p *= n
	return p

def least_common_multiple_v1(maxDivisor):
	"""
	>>> least_common_multiple_v1(10)
	2520
	>>> least_common_multiple_v1(20)
	232792560
	"""
	primeFactorsCounter = Counter()
	for divisor in range(1, maxDivisor+1):
		# Get the union of the currently-used prime factors and the prime factors of divisor.
		primeFactorsCounter |= Counter(Prime.prime_factors(divisor))
	return product(primeFactorsCounter.elements())

if __name__ == "__main__":
	import doctest
	doctest.testmod()

	maxDivisor = 20
	print("The smallest positive number that is evenly divisible by all of the numbers from 1 to {:,} (least common multiple) is:".format(maxDivisor))
	print("Method 1: {}".format(least_common_multiple_v1(maxDivisor)))
