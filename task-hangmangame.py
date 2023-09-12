import random

print("Let's play Hangman!")

words = ['rainbow', 'computer', 'science', 'programming',
		'python', 'mathematics', 'player', 'condition',
		'reverse', 'water', 'board', 'geeks']

word = random.choice(words)


print("Guess a letter: ")
guesses = ''
turns = 12
while turns > 0:

	failed = 0

	for char in word:

		if char in guesses:
			print(char, end=" ")

		else:
			print("_")

			failed += 1

	if failed == 0:
		print("Congratulations! You guessed the word: ", word)
		break

	print()
	guess = input("guess a letter: ")

	guesses += guess

	if guess not in word:

		turns -= 1

		print("Wrong")

		print("You have", + turns, 'more guesses')

		if turns == 0:
			print("You Lose")
