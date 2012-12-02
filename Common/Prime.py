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
	[2, 2, 2]
	>>> prime_factors(143)
	[11, 13]
	>>> prime_factors(2431)
	[11, 13, 17]
	>>> prime_factors(13195)
	[5, 7, 13, 29]
	"""
	product = n
	prime_factors = []
	factor = 2
	newProduct = True
	while True:
		if newProduct:
			newProduct = False
			maxFactor = ceil(sqrt(product))

		if factor > maxFactor:
			break

		if (product % factor == 0) and is_prime(factor):
			prime_factors.append(factor)

			# Update the product.
			product //= factor
			newProduct = True

			# Allow multiples of the same factor.
			factor -= 1

		factor += 1

	# Handle the last prime factor.
	if product != 1:
		prime_factors.append(product)

	return prime_factors

if __name__ == "__main__":
	import doctest
	doctest.testmod()