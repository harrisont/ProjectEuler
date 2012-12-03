def sum_of_squares(n):
	"""
	>>> sum_of_squares(10)
	385
	""" 
	return sum([x**2 for x in range(n + 1)])

def square_of_sum(n):
	"""
	>>> square_of_sum(10)
	3025
	"""
	return sum(range(n+1)) ** 2

def difference_between_sum_of_squares_and_square_of_sum_v1(n):
	"""
	>>> difference_between_sum_of_squares_and_square_of_sum_v1(10)
	2640
	>>> difference_between_sum_of_squares_and_square_of_sum_v1(100)
	25164150
	""" 
	return square_of_sum(n) - sum_of_squares(n)

if __name__ == '__main__':
	import doctest
	doctest.testmod()

	n = 100
	print("The difference between the sum of the squares of the first {:,} natural numbers and the square of the sum is:".format(n))
	print("Method 1: {}".format(difference_between_sum_of_squares_and_square_of_sum_v1(n)))
