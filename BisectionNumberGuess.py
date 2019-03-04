#BisectionNumberGuess
print("Please think of a number between 0 and 100!")
ming = 0
maxg = 100
guess = 50
hint = "d"
while True :
	print("Is your secret number "+str(guess)+"?")
	hint = str.lower(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))
	if hint == "c":
		break
	elif hint == "l":
		ming = guess
	elif hint== "h":
		maxg = guess
	else:
		print("Please give me a 'h','l'or'c'!")
		continue
	guess = (ming+maxg)//2
print("Game over. Your secret number was: "+str(guess))

