def is_palindrome(s):
	"""
	>>> is_palindrome("a")
	True
	>>> is_palindrome("ab")
	False
	>>> is_palindrome("abba")
	True
	>>> is_palindrome("12321")
	True
	"""
	length = len(s)
	for indexLeft in range((length + 1) // 2):
		indexRight = length - indexLeft - 1
		if s[indexLeft] != s[indexRight]:
			return False
	return True

def larget_product_palindrome_v1(digits):
	"""
	>>> larget_product_palindrome_v1(2)
	(9009, (99, 91))
	>>> larget_product_palindrome_v1(3)
	(906609, (993, 913))
	"""
	largestProductPalindrome = 0
	factors = (0, 0)
	upper = 10**digits - 1
	lower = 10**(digits - 1)
	for a in range(upper, lower - 1, -1):
		for b in range(a, lower - 1, -1):
			product = a * b
			if product > largestProductPalindrome and is_palindrome(str(a * b)):
				largestProductPalindrome = product
				factors = (a, b)
	return largestProductPalindrome, factors

if __name__ == "__main__":
	import doctest
	doctest.testmod()

	digits = 4
	print("The largest palindrome made from the product of two {:,}-digit numbers is:".format(digits))
	product1, (a1, b1) = larget_product_palindrome_v1(digits)
	print("Method 1: {} ({} * {})".format(product1, a1, b1))
