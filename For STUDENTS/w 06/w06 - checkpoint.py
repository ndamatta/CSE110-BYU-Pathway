# https://byui-cse.github.io/cse110-course/lesson06/checkpoint.html
# 06 Prepare: Checkpoint

print("--------QUALIFYING FOR LOAN--------")
print("Please answer the following questions rating from 1 to 10:")

#INPUTS AND VARIABLES
loan_large = int(input("How large is the loan?: "))
credit_history = int(input("How good is your credit history?: "))
income = int(input("How high is your income?: "))
down_payment = int(input("How large is your down payment?: "))

qualify_for_loan = False


#CONDITIONALS
if loan_large >= 5:

    if credit_history >= 7 and income >= 7:
        qualify_for_loan = True
    
    elif (credit_history >= 7 or income >= 7) and down_payment >= 5:
        qualify_for_loan = True

    else:
        qualify_for_loan = False
    
else:
    if credit_history < 4:
        qualify_for_loan = False
    
    elif income >= 7 or down_payment >= 7:
        qualify_for_loan = True 
    
    elif income >= 4 and down_payment >= 4:
        qualify_for_loan = True 

    else:
        qualify_for_loan = False

#DISPLAY OUTPUT
if qualify_for_loan:
    print("\nYES. You qualify for a loan")

else:
    print("\nNO. You don't qualify for a loan")

print("----------------------------")