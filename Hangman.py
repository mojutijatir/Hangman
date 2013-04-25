#Hangman Game

import random
import string

WORD_LIST = "words.txt"

def loadWords():
  '''
	Returns a list of valid words. Words are strings of lower case letters.
	Depending on the size of the word list, this function may
	take a while to finish.
	'''
	
	print "Loading word list from file..."
	#inFile: file
	inFile = open(WORD_LIST, 'r', 0)
	#line: string
	line = inFile.readline()
	#wordlist: list of strings
	wordlist = string.split(line)
	print " ",len(wordlist), "words loaded."
	return wordlist

def chooseWord(worlist):
	'''
	wordlist(list): list of words(strings)
	
	Returns a word from wordlist at random
	'''
	return random.choice(wordlist)

#end of helper code
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
	'''
	secretWord: string, the word the user is guessing
	lettersGuessed: list, what letters have been guessed so far
	returns: boolean, True, if all the letters of secretWord are in lettersGuessed;
		False otherwise
	'''
	yes = []
	no = []
	for char in lettersGuessed:
		if char in secretWord:
			count = 0
			for i in range(len(secretWord)):
				if secretWord[i] == char:
					count += 1
			for i in range(count):
				yes.append(char)
		else:
			no.append(char)
	
	if len(yes) == len(secretWord):
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
    l = []
    for char in lettersGuessed:
        if char in secretWord:
            l.append(char)
    strng = ''
    for s in range(len(secretWord)):
        if secretWord[s] in l:
            strng = strng + secretWord[s] + " "
        else:
            strng = strng + "_ "
    return strng


def getAvailableLetters(lettersGuessed):
	'''
	lettersGuessed: list, what letters have been guessed so far
	returns: string, comprised of letters that represents what letters have
		not been guessed yet
	'''
	strng = string.ascii_lowercase
	s = ''
	for char in strng:
		if char not in lettersGuessed:
			s = s + char
	return s


def hangman(secretWord):
	print "\nWelcome to the game, Hangman!"
	print "I am thinking of a word that is",len(secretWord),"letters long."
	print "-------------"
	
	no_of_guesses = 8
	lettersGuessed = []
	
	while no_of_guesses > 0:
		print "You have",no_of_guesses,"guesses left."
		av_letters = getAvailableLetters(lettersGuessed)
		print "Available letters:",av_letters
		guess = raw_input("Please guess a letter: ")
		guess = guess.lower()
		
		#warn if letter already guessed
		if guess in lettersGuessed:
			word_so_far = getGuessedWord(secretWord, lettersGuessed)
			print "Oops! You've already guessed that letter:",word_so_far
		elif guess in secretWord:
			lettersGuessed.append(guess)
			word_so_far = getGuessedWord(secretWord, lettersGuessed)
			print "Good guess:",word_so_far
		else:
			lettersGuessed.append(guess)
			word_so_far = getGuessedWord(secretWord, lettersGuessed)
			print "Oops! That letter is not in my word:",word_so_far
			no_of_guesses -= 1
		
		print "------------"
		
		#check if player won
		if isWordGuessed(secretWord, lettersGuessed):
			break
	
	#to print final output
	if isWordGuessed(secretWord, lettersGuessed):
		print "Congratulations, you won!\n"
	else:
		print "Sorry, you ran out of guesses. The word was",secretWord,"\n"
		


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

