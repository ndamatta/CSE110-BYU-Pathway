# https://byui-cse.github.io/cse110-course/lesson09/prove.html
# 09 Prove: Assignment Milestone

#VARIABLES
items = []
user_input_menu = 0
user_input_item = ""

#PROGRAM LOOP (IF 5 THEN QUIT)
while user_input_menu != 5: 

    #PRINT MENU AND USER INPUT
    print("\nPlease select one of the following:")
    print("1. Add an item\n2. View Cart\n3. Remove item\n4. Compute total\n5. Quit")
    user_input_menu = int(input("Please, enter an action: "))
    
    #CONDITIONALS
    if user_input_menu == 1: # 1. ADD ITEM

        user_input_item = input("What item would you like to add: ")
        items.append(user_input_item)
        print(f"'{user_input_item}'  has been added correctly!")
    
    elif user_input_menu == 2: # 2. VIEW CART
        
        print("The items in the cart are:")
        for item in items:
            print(item)


#QUIT MSG
print("\nThanks for operating our software, bye!")   
    

