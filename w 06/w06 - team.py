# https://byui-cse.github.io/cse110-course/lesson06/teach.html
# 06 Teach: Team Activity

print("---------------")
#BOOLEANS
can_ride = False
have_golden_ticket = False

#USER INPUT
first_rider_age = int(input("What's the age of the first rider?: "))
first_rider_height = int(input("What's the height of the first rider?: "))
second_rider = input("Is there a second driver? (YES / NO): ")

#CONDITIONALS
if second_rider.upper() == "YES":

    second_rider_age = int(input("What's the age of the second rider?: "))
    second_rider_height = int(input("What's the height of the second rider?: "))

    if first_rider_height < 36 or second_rider_height < 36:
        can_ride = False
    
    else:
        if first_rider_age >= 18 or second_rider_age >= 18:
            can_ride = True
        else: 
            golden_ticket = input("Do you have a golden ticket? (YES / NO): ")
            if golden_ticket.upper() == "yes" and (first_rider_height > 63 and second_rider_height > 63):
                can_ride = True
            else:              
                if (first_rider_age >= 16 and second_rider_age >= 14) or (first_rider_age >= 14 and second_rider_age >= 16):
                    can_ride = True
                else:
                    can_ride = False
            

            if (first_rider_age >= 12 and second_rider_age >= 12) and (first_rider_height >= 52 and second_rider_height >= 52):
                can_ride = True
            else:
                can_ride = False
elif second_rider.upper() == "NO":
    
    if first_rider_height < 36:
        can_ride = False
    
    else:
        if first_rider_age >= 18 and first_rider_height >= 63:
            can_ride = True
        
        else:
            golden_ticket = input("Do you have a golden ticket? (YES / NO): ")

            if golden_ticket.upper() == "yes" and first_rider_height > 63:
                    can_ride = True

            else:
                can_ride = False

#OUTPUT
else:
    print("Invalid data")


if can_ride:
    print("You can ride!")
else:
    print("Sorry, you can't drive!")

print("---------------")
    
 





