#StringTest&Compare
if type(varA) == type("A") or type(varB) == type("A"):
	print("string involved")
else:
	if varA == varB:
		print("equal")
	elif varA > varB:
		print("bigger")
	elif varA < varB:
		print("smaller")
	else:
		print("error")