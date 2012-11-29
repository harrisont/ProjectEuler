from math import sqrt, ceil
from functools import lru_cache

@lru_cache(maxsize=None)
def is_prime(n):
	"""
	>>> is_prime(0)
	True
	>>> is_prime(1)
	True
	>>> is_prime(2)
	True
	>>> is_prime(3)
	True
	>>> is_prime(4)
	False
	>>> is_prime(7)
	True
	>>> is_prime(9)
	False
	"""
	upperBound = min(n, 1 + ceil(sqrt(n)))
	for factor in range(2, upperBound):
		if n % factor == 0:
			return False
	return True

def prime_factors(n):
	"""
	>>> prime_factors(6)
	[2, 3]
	>>> prime_factors(8)
	[2]
	>>> prime_factors(13195)
	[5, 7, 13, 29]
	"""
	prime_factors = []
	for factor in range(2, 1 + ceil(sqrt(n))):
		if (n % factor == 0) and is_prime(factor):
			prime_factors.append(factor)
	return prime_factors

def larget_prime_factor_v1(n):
	"""
	>>> larget_prime_factor_v1(6)
	3
	>>> larget_prime_factor_v1(8)
	2
	>>> larget_prime_factor_v1(13195)
	29
	"""
	return max(prime_factors(n))

if __name__ == "__main__":
	import doctest
	doctest.testmod()

	n = 600851475143# * 2*1009
	print("The largest prime factor of {:,} is:".format(n))
	print("Method 1: {}".format(larget_prime_factor_v1(n)))
