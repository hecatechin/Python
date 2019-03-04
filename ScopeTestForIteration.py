#ScopeTestForIteration
num = 10
print(id(num))
for num in range(5):
	print(num)
	print(id(num))
print(num)
print(id(num))