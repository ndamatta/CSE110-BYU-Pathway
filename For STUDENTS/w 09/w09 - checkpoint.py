# https://byui-cse.github.io/cse110-course/lesson09/checkpoint.html
# 09 Prepare: Checkpoint

#LIST AND INPUT
friends = []
user_input = ""

#CONDITIONAL
while user_input.capitalize() != "End":
    user_input = input("What's your friend's name?: ")
    
    if user_input.capitalize() != "End":
        friends.append(user_input.capitalize())

#OUTPUT
print("Your friends are:")
for friend in friends:
    print(friend)
