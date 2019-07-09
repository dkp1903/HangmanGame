# Python program to implement Hangman game 

# Importing random module 
import random 

# Function to randomly select 
# a word from dictionary 
def get_word(): 
	
	# Path to the text file 
	with open('/Users/Admin/Desktop/words.txt', 'r') as f: 
		
		# Reads each word after splitting 
		words1 = f.read().splitlines() 
	
	# Returns any random word	 
	return random.choice(words1) 

myword = get_word() 

# Function prints row of 
# stars in place of words 
for i in myword: 
	
	print("*", end = " ") 
	
# Calculating length of word 
l = len(myword) 
print("\nWord has %d letters" %l) 

# Check if entered letter is correct 
def check(myword, your_word, guess1): 
	status = '' 
	matches = 0
	
	for letter in myword: 
		if letter in your_word: 
			status += letter 
		else: 
			status += '*'
		if letter == guess1: 
			matches += 1
			
	if matches > 1: 
		print(matches, guess1) 
		
	elif matches == 1: 
		print(guess1) 
	return status 

# Main Game function 
def game(): 
	guess = 0
	guessed = False
	your_word = [] 
	turns = len(myword) + 1
	turns1 = turns 
	
	print("Total turns: ", turns) 
	while guess < turns1: 
		guess1 = input("Enter your guess: ") 
		
		# Decrementing turn 
		# after every guess 
		turns -= 1
		
		# Print turns left 
		print("Turns left", turns) 
		
		# If letter is already guessed 
		if guess1 in your_word: 
			print("You already guessed") 
		elif len(guess1) == 1: 
			
			# Appending the letters 
			# on their place 
			your_word.append(guess1) 
			result = check(myword, your_word, guess1) 
			
			if result == myword: 
				guessed = True
				print("You won " + name) 
				print(myword) 
			else: 
				print(result) 
		else: 
			print("Invalid entry") 
		guess += 1
	if guess == turns1: 
		print("Word is:") 
		print(myword) 

# Driver Code 
game() 
