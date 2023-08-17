# https://byui-cse.github.io/cse110-course/lesson07/prove.html
# 07 Prove: Assignment Milestone

print("--------------------------------------")
print("---WORD GUESSING GAME---\nThere is a hidden word, you must guess what it is...")

#VARIABLES AND INPUT
guesses = 0
secret_word = "TABLE"
user_guess = input("What's your guess?: ")
 
#WHILE LOOP
while user_guess.upper() != secret_word:
    print("\nYour guess was not correct")

    user_guess = input("What's your guess?: ")

    guesses += 1

#FINAL
print("\nCongratulations! You guessed the word")
print(f"It took you {guesses} guesses")
print("--------------------------------------")
