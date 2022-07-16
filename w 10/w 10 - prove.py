# https://byui-cse.github.io/cse110-course/lesson09/prove.html
# 10 Prove: Assignment - Shopping Cart

#VARIABLES
items = []
prices = []
total_price = 0
total_item = 0

user_input_menu = 0
user_input_item = ""
user_input_number = 0

#PROGRAM LOOP (IF 6 THEN QUIT)
while user_input_menu != 6: 

    #PRINT MENU AND USER INPUT
    print("\nPlease select one of the following:")
    print("1. Add an item\n2. View Cart\n3. Remove item\n4. Compute total price\n5. Compute number of items\n6. Quit")
    user_input_menu = int(input("Please, enter an action: "))
    
    #CONDITIONALS MENU
    if user_input_menu == 1: # 1. ADD ITEM
        #USER INPUTS
        user_input_item = input("What item would you like to add: ")
        user_input_number = float(input(f"What is the price of '{user_input_item}'?: "))

        #ADD ITEM AND PRICE TO LISTS AND PRINT MSG
        items.append(user_input_item)
        prices.append(user_input_number)
        print(f"'{user_input_item}'  has been added correctly!")
    
    elif user_input_menu == 2: # 2. VIEW CART
        
        #IF CART IS EMPTY
        if items == [] and prices == []:
            print("Your cart is empty!")

        #IF CART HAS ITEMS
        else:
            print("\nThe items in the cart are:")
            #ITERATE ITEMS AND PRICES
            for index in range(len(items)) and range(len(prices)):
                item = items[index]
                price = prices[index]

                print(f"{index + 1}. {item} - ${price:.2f}")
    
    elif user_input_menu == 3: # 3. REMOVE ITEM
        user_input_number = int(input("Which item would you like to remove?: "))
        items.pop(user_input_number - 1)
        prices.pop(user_input_number - 1)

        print("Item removed!")

    elif user_input_menu == 4: # 4. COMPUTE TOTAL PRICE ROUNDED
        #ITERATE PRICES
        for number in prices:
            total_price += number

        print(f"The total price of the items in the shopping cart is: ${total_price:.2f}")

    elif user_input_menu == 5: # 5. COMPUTE TOTAL ITEM
        #ITERATE ITEMS
        for number in range(len(items)):
            total_item = number

        #IF CART IS EMPTY
        if total_item == 0 and items == [] and prices == []:
            print("Your cart is empty!")

        #IF CART HAS ITEMS    
        else:
           print(f"You have {total_item + 1} items in you cart!") 
  
#QUIT MSG
print("\nThanks for operating our software, bye!")   
    

