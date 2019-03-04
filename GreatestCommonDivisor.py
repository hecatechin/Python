#GreatestCommonDivisor
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    divisor = min (a, b)
	while a%divisor != 0 or b%divisor != 0 :
		if divisor == 1:
			break
		divisor -=1
	return divisor

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    divisor = min (a, b)
	if divisor == 0:
		return a
	else :
		return gcdRecur(b, a%b)