import random
import hangman_art as ha
import hangman_words


chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


print(ha.logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
guessstr=""
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in guessstr :
      print("You've already guessed this letter")
    else:
    #Check guessed letter
      for position in range(word_length):
          letter = chosen_word[position]
          if letter == guess:
              display[position] = letter
  
      #Check if user is wrong.
      if guess not in chosen_word:
          print("Letter not in word")
          lives -= 1
          if lives == 0:
              end_of_game = True
              print("You lose.")
  
      #Join all the elements in the list and turn it into a String.
      print(f"{' '.join(display)}")
  
      #Check if user has got all letters.
      if "_" not in display:
          end_of_game = True
          print("You win.")
      # prints the ascii art
      print(ha.stages[lives])
      guessstr+=guess
