# https://byui-cse.github.io/cse110-course/lesson07/checkpoint.html
# 07 Prepare: Checkpoint

#USER INPUT
number = int(input("Please enter a positive number: "))

#CONDITIONAL
while number < 0:
    print("That's a negative number, please try again")
    number = int(input("Please enter a positive number: "))

print("Valid number!")

#USER INPUT
decision = input("Can I have a candy?: ")

#CONDITIONAL
while decision.upper() == "NO":
    decision = input("Can I have a candy?: ")

print("Thanks")
