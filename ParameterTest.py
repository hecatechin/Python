#parameter test
#test if a parameter had asigned a type, can it be redefined
def fact(n,m=1):
	s=1
	for i in range(1,n+1):
		s+=i
	return s+m
print(fact(10,'sw'))