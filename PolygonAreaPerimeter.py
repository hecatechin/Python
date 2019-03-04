#PolygonAreaPerimeter
import math
def polysum(n, s):
	'''
		in: 
			n int, n>=3, 
			s, int or float, s>0
		out:  
			sum the area and square of the perimeter of the regular polygon.
			rounded to 4 decimal places.
	'''
	return round(polyarea(n,s) + polyperimeter(n, s) ** 2 , 4)

def polyarea(n, s):
	# returns the area of polygon has n number of sides. Each side has length s.
	return 0.25*n*s*s/math.tan(math.pi/n)

def polyperimeter(n, s):
	# returns the perimeter of polygon has n number of sides. Each side has length s.
	return n*s