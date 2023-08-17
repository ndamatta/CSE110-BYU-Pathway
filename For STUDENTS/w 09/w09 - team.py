# https://byui-cse.github.io/cse110-course/lesson09/teach.html
# 09 Teach: Team Activity


#VARIABLES

is_running = True
numbers = []
user_number = 0
largest = 0
smallest = 9999999
avarage = 0
sum = 0

#WHILE PROGRAM LOOP
while is_running:

    user_number = int(input("Please, enter your number: "))

    if user_number != 0:
        numbers.append(user_number)
    
    else:
        is_running = False

#SUM
for number in numbers:

    sum += number
print(f"The sum is: {sum}")

#AVARAGE
print("The avarage is", sum / len(numbers))

#LARGEST
for number in numbers:

    if number > largest:
        largest = number
print(f"The largest number is: {largest}")

#SMALLEST
for number in numbers:

    if number < smallest and number > 0:
        smallest = number
print(f"The smallest positive number is: {smallest}")

#SORT
numbers.sort()
print(f"Your sorted list is: {numbers}")