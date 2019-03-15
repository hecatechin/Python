# Hangman game

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    lg = lettersGuessed
    num = 0
    for c in secretWord:
        if c in lg:
            num += 1
    if num == len(lg):
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    lg = lettersGuessed
    result = ""
    for c in secretWord:
        if c in lg:
            result += c
        else:
            result += "_"
    return result


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    lg=lettersGuessed
    lista = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for c in lista:
        if c not in lg:
            result += c
    return result
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is "+str(len(secretWord))+" letters long.")

    lefttime = 10
    lettersGuessed = []
    lg = lettersGuessed

    while lefttime > 0:
        print("You have %d guesses left." % lefttime)
        print("Available letters: "+ getAvailableLetters(lg))

        letter = input("Please guess a letter: ").lower()

        if letter not in lg:
            lg.append(letter)
            if letter in secretWord:
                print("Good guess: "+getGuessedWord(secretWord,lg))
            else:
                lefttime -= 1
                print("Oops! That letter is not in my word: "+getGuessedWord(secretWord,lg))
        else:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lg))
        print("------------")

        if getGuessedWord(secretWord,lg) == secretWord:
            break

    if getGuessedWord(secretWord,lg) == secretWord:
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was %s." % secretWord)

secretWord = chooseWord(wordlist)
hangman(secretWord)