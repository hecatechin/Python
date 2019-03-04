#StringFunctionExercises
def countVowel(s):
	vowels=0
	for char in s:
		if char=="a" or char=="e" or char=="i" or char=="o" or char=="u":
			vowels+=1
	return vowels

def countbob(s):
	bobs=0
	indexs = 0
	for indexs in range(len(s)-2):
		if s[indexs]=="b" and s[indexs+1]=="o" and s[indexs+2]=="b":
			bobs+=1
		indexs+=1
	return bobs


def alpha(s):
	i = 0
	temp=""
	maxs=""
	maxstemp=s[0]
	for char in s:
		if char >= temp:
			maxstemp += char
		elif len(maxstemp) > len(maxs):
			maxs=maxstemp
		else:
			maxstemp=char
		temp = char
	return maxs

s=input("input a str: ")
print(alpha(s))
print("Number of vowels:", countVowel(s))
print('Number of "bob" is:', countbob(s))