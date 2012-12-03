if __name__ == "__main__":
	import sys
	sys.path.insert(0, '..')
from Common import Prime

from math import sqrt, ceil

def get_prime_v1(primePosition):
	"""
	>>> get_prime_v1(6)
	13
	"""
	n = 3
	primeNumbersSeen = 1 # 2 is prime
	while True:
		if Prime.is_prime(n):
			primeNumbersSeen += 1
			if primeNumbersSeen == primePosition:
				return n
		n += 2

def get_prime_v2(primePosition):
	"""
	Sieve the numbers.

	>>> get_prime_v2(6)
	13
	"""
	maxCandidate = 64
	minPrime = 3

	primes = [2]
	nonPrimes = set()

	while primePosition > len(primes):
		maxCandidate *= 2

		for factor in range(2, 1 + ceil(sqrt(maxCandidate))):
			if Prime.is_prime(factor):
				nonPrime = factor * 2
			else:
				nonPrime = factor

			while nonPrime <= maxCandidate:
				nonPrimes.add(nonPrime)
				nonPrime += factor

		primes.extend([n for n in range(minPrime, maxCandidate+1, 2) if n not in nonPrimes])
		minPrime = maxCandidate + 1
	
	return primes[primePosition - 1]

if __name__ == '__main__':
	import doctest
	doctest.testmod()

	primePosition = 10001
	print("The {:,}th prime is:".format(primePosition))
	#print("Method 1: {}".format(get_prime_v1(primePosition)))
	print("Method 2: {}".format(get_prime_v2(primePosition)))
	# get_prime(10001) == 104743