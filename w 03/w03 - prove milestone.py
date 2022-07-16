# https://byui-cse.github.io/cse110-course/lesson03/prove.html
# 03 Prove: Milestone - Meal Price Calculator

print ("-----------MEAL PRICE CALCULATOR-----------")
#INPUTS
child_meal_price = float(input("What is the price of a child's meal?: "))
adult_meal_price = float(input("What is the price of a adult's meal?: "))
child_quantity = int(input("How many children are there?: "))
adult_quantity = int(input("How many adults are there?: "))
sales_tax_rate = float(input("What is the sales tax rate?: "))
tip_percentage = float(input("What is the tip percentage?: "))
print ()

#SUBTOTAL
subtotal = (child_quantity * child_meal_price) + (adult_quantity + adult_meal_price)
print (f"Subtotal: ${subtotal:.2f}")

#SALES TAX
sales_tax = subtotal * sales_tax_rate / 100
print (f"Sales Tax: ${sales_tax:.2f}")

#TIP
tip = subtotal * tip_percentage / 100
print (f"Tip: ${tip:.2f}")

#TOTAL
total = subtotal + tip + sales_tax
print (f"Total: ${total:.2f}")
print()

#PAYMENT
payment_amount = float(input("What is the payment amount?: "))

while payment_amount <= total:
    print ("That's not enough money, please insert a valid amount...")
    payment_amount = float(input("What is the payment amount?: "))

#CHANGE
change = payment_amount - total
print (f"Change: ${change:.2f}")
print ("----------------------")


input("Press enter to quit...")