# https://byui-cse.github.io/cse110-course/lesson13/teach.html
# 13 Teach: Team Activity

#FUNCTIONS
def compute_area_square(area):
    area_square = area ** 2
    return area_square

def compute_area_rectangle(lenght, width):
    area_rectangle = lenght * width
    return area_rectangle

def compute_area_circle(radius):
    area_circle = 3.14 * (radius ** 2)
    return area_circle

#VARIABLES
user_input = ""
number1 = None
number2 = None

#CONDITIONAL
print("---SHAPE CALCULATOR---")
while user_input.lower() != "quit":
    
    print("\nShapes: \n1. Square \n2. Rectangle \n3. Circle")
    user_input = input("Type a shape:")

    match user_input.lower():

        case "square":
            number1 = int(input("What's the area of the square?: "))
            print()
            print(f"The area of the square is: {compute_area_square(number1)}")
        
        case "rectangle":
            number1 = int(input("What's the lenght of the square?: "))
            number2 = int(input("What's the width of the square?: "))
            print()
            print(f"The area of the rectangle is: {compute_area_rectangle(number1,number2)}")
  
        case"circle":
            number1 = int(input("What's the radius of the circle?: "))
            print()
            print(f"The area of the circle is: {compute_area_circle(number1)}")
