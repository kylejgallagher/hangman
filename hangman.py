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


randomword = random.choice(word_list)
print (randomword)

display = "_" * len(randomword)
print(display)

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
