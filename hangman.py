from multiprocessing.pool import worker
word_list = ["aardvark", "baboon", "camel"]
import random



stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
randomword = random.choice(word_list)
print (randomword)

display = "_" * len(randomword)
print(display)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.



# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.



lives = 6


while "_" in display:
    guess = input("Guess a letter ").lower()
    if guess in randomword:
        print("Right")
        new_display = ""
        for i in range(len(randomword)):
            if randomword[i] == guess:
                new_display += guess
            else:
                new_display += display[i]
        display = new_display
        print(stages[lives])
    else:
        lives -= 1
        print(f"Wrong! you have {lives} lives left")
        print(stages[lives])
  
    if lives == 0:
        print(f"You lose! :-( The word was {randomword}")
        break
    print(display)
  
    if display == randomword:
        print("You won the game!")
        break

