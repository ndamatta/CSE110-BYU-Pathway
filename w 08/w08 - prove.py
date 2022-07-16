# https://byui-cse.github.io/cse110-course/lesson07/prove.html
# 08 Prove: Assignment - Word Games
import random

#START
print("--------------------------------------")
print("---WORD GUESSING GAME---\nThere is a hidden word, you must guess what it is...")
print("You only have 5 guesses")

#VARIABLES
word_list = ["spoon", "table", "chair", "mouse", "watch", "light", "model", "paper"]
secret_word = random.choice(word_list)
guesses = 0
hint = ""
position = 0


#INITIAL HINT
print("\nYour hint is: " + " _ " * len(secret_word))

#USER GUESS INPUT
user_guess = input("What's your guess?: ")
guesses += 1

#GAME WHILE LOOP
while user_guess.lower() != secret_word and guesses <=5:
    print("\nWrong guess!")  
    
    #CHECK SECRET WORD AND USER GUESS
    for char in user_guess:
        
        #CATCH ERROR IF 5+ LETTERS
        try:

            #CONDITIONALS
            if char == secret_word[position]: #CAPS LETTERS
                hint +=  " " + char.upper() + " "
            
            elif char in secret_word: #LOWER LETTERS
                hint +=  " " + char.lower() + " "

            else: #UNDERLINES
                hint += " _ " 

        except:

            print("More than 5 letter words aren't allowed. Try again!")
            hint = " _ " * len(secret_word) #store the initial hint in the hint variable
            break

        position += 1

    print(f"Your hint is: {hint}")        
    user_guess = input("What's your guess?: ")
    
    #RESET VARIABLES
    hint = ""
    position = 0
    guesses += 1

#FINAL
if guesses == 5:
    print("\nYou didn't guess the word! GAME OVER")

else:
    print("\nCongratulations! You guessed the word")
    print(f"It took you {guesses} guesses")
    print("--------------------------------------")
