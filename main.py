import random
from hangman_words import word_list
from hangman_art import logo, stages

print(logo)

chosen_word = random.choice(word_list)
#Or chosen_word = word_list[random.randint(0, len(word_list) - 1)]
end_of_game = False
lives = 6

# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks in display according to length of word
display = []
for _ in range(len(chosen_word)):
    display += "_"

wrong_guess = []      
while end_of_game == False:
    guess = input("Guess a letter: ").lower()
    #Handle the case where the user accidentally enters more than one letter or anthing other than a letter.
    if len(guess) >1 or guess.isalpha() == False:
        print("please enter only one single letter of the alphabet at any one time!")
    else:
      #Check if letter already guessed right
      if guess in display:
        print(f"You have entered '{guess}', which you already guessed right.")
  
      #Check guessed letter. Loop through each position in the chosen_word; If the letter at that position matches 'guess' then reveal that letter in the display at that position.
      for i in range(len(chosen_word)):
          letter = chosen_word[i]
          # #see the loop
          # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}") 
          if letter == guess:
              display[i] = letter
  
      #Check if user is wrong. End game if user loses all lives. Add wrong letters already guessed in wrong guess list.Check if already guessed wrong  
      if (guess not in chosen_word) and (guess not in wrong_guess):         
        print(f"You have entered '{guess}' which is not in the word. You lose one life.")
        lives -= 1
        if lives == 0:
          end_of_game = True
          print("You lose.")
          
        wrong_guess += guess 
       
      #for letters already guessed wrong
      elif (guess not in chosen_word) and (guess in wrong_guess):
        print(f"You have entered '{guess}', which you already guessed wrong.")        
  
      #Join all the elements in the list and turn it into a String.
      print(f"{' '.join(display)}")
  
      #Check if user has got all letters.
      if "_" not in display:
          end_of_game = True
          print("You win.")
  
      print(stages[lives])
