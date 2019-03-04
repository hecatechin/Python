#TemConvert.py
TempStr = input("type in temp with chart please:")
if TempStr [-1] in ['F','f']:
	C = (eval(TempStr[0: -1]) - 32)/1.8
	print('tansformed temp is : {:.2f}C'.format(C))
elif TempStr[-1] in ['C','c']:
	F = 1.8*eval(TempStr[0: -1]) + 32
	print('transformed temp is : {:.2f}F'.format(F))
else:
	print('error!')