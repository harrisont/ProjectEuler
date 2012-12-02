if __name__ == "__main__":
	import sys
	sys.path.insert(0, '..')
from Common import Prime

def larget_prime_factor_v1(n):
	"""
	>>> larget_prime_factor_v1(6)
	3
	>>> larget_prime_factor_v1(8)
	2
	>>> larget_prime_factor_v1(13195)
	29
	"""
	return max(Prime.prime_factors(n))

if __name__ == "__main__":
	import sys
	sys.path.insert(0, '..')

	import doctest
	doctest.testmod()

	n = 600851475143# * 2*1009
	print("The largest prime factor of {:,} is:".format(n))
	print("Method 1: {}".format(larget_prime_factor_v1(n)))
