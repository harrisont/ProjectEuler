def greatest_consecutive_digits_product_v1(numDigits, searchNum):
	"""
	>>> greatest_consecutive_digits_product_v1(2, "1234321")
	12
	>>> greatest_consecutive_digits_product_v1(3, "12345")
	60
	>>> greatest_consecutive_digits_product_v1(3, "54321")
	60
	>>> greatest_consecutive_digits_product_v1(2, "32156")
	30
	>>> greatest_consecutive_digits_product_v1(2, "320079")
	63
	"""
	product = 1
	maxProduct = 0
	numZeros = 0

	# Calculate the product of the first numDigits digits.
	for i in range(numDigits):
		n = int(searchNum[i])
		if n > 0:
			product *= n
		else:
			numZeros += 1
	if numZeros == 0:
		maxProduct = product

	for i in range(len(searchNum) - numDigits):
		# Calculate the product of digits [i+1, i+numDigits]
		# by undoing digit i and adding digit i+numDigits.
		left = int(searchNum[i])
		right = int(searchNum[i+numDigits])
		if left > 0:
			product //= left
		else:
			numZeros -= 1
		if right > 0:
			product *= right
		else:
			numZeros += 1

		maxProduct = max(product, maxProduct)

	return maxProduct

def greatest_consecutive_digits_product_v2(numDigits, searchNum):
	"""
	>>> greatest_consecutive_digits_product_v2(2, "1234321")
	12
	>>> greatest_consecutive_digits_product_v2(3, "12345")
	60
	>>> greatest_consecutive_digits_product_v2(3, "54321")
	60
	>>> greatest_consecutive_digits_product_v2(2, "32156")
	30
	>>> greatest_consecutive_digits_product_v2(2, "320079")
	63
	"""
	maxProduct = 0
	for i in range(len(searchNum) - numDigits + 1):
		product = 1
		for j in range(numDigits):
			product *= int(searchNum[i + j])
		maxProduct = max(product, maxProduct)
	return maxProduct

if __name__ == '__main__':
	import doctest
	doctest.testmod()

	numDigits = 5
	searchNum = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
	print("The greatest product of {} consecutive digits in {} is:".format(numDigits, searchNum))
	print("Method 1: {}".format(greatest_consecutive_digits_product_v1(numDigits, searchNum)))
	print("Method 2: {}".format(greatest_consecutive_digits_product_v2(numDigits, searchNum)))