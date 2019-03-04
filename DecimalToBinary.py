#Decimal to binary
def decimalToBinary(x):
	'''
		in: a float between 0 to 1
		out: a string that format as 0b0.101 that stands for the binary of the number input
	'''
	p = 0
	n = 0
	while ( (2**p)*x ) % 1 != 0:
		n += 1
		print("Remainder = " + str( (2**p)*x -int( (2**p)*x) ) + " Circle= " + str(n) )
		p += 1
	num = int((2**p)*x)
	result = ""
	if num == 0:
		result = "0"
	while num > 0:
		result = str(num%2) + result
		num = num//2
	for i in range(p - len(result) ):
	result = "0" + result
	result = "0."+result
	return "0b"+result
