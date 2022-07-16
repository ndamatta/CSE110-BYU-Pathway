# https://byui-cse.github.io/cse110-course/lesson10/checkpoint.html
# 10 Prepare: Checkpoint

items = []
user_item = ""

while user_item.upper() != "QUIT":

    user_item = input("Please enter a new item. Type 'quit' to exit: ")
    
    if user_item.upper() != "QUIT":
        items.append(user_item)

    else:
        break

print("The shopping list is: ")
for item in items:
    print(item)

print("\nThe shopping list with index is: ")
for i in range(len(items)):
    item = items[i]
    print(i + 1,". ", item)

user_number = int(input("What item would you like to change?: "))
user_item = input("What is the new item: ")

items.pop(user_number - 1)
items.insert(user_number - 1, user_item)

print("\nThe shopping now is:")
for i in range(len(items)):
    item = items[i]
    print(i + 1,". ", item)
