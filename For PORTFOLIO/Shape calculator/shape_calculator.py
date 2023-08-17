#FUNCTIONS
def compute_area_square(area):
    return area ** 2

def compute_area_rectangle(lenght, width):
    return lenght * width

def compute_area_circle(radius):
    return 3.14 * (radius ** 2)

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
            print(f"The area of the square is: {compute_area_square(number1)}")
        
        case "rectangle":
            number1 = int(input("What's the lenght of the square?: "))
            number2 = int(input("What's the width of the square?: "))
            print(f"The area of the rectangle is: {compute_area_rectangle(number1,number2)}")
  
        case"circle":
            number1 = int(input("What's the radius of the circle?: "))
            print(f"The area of the circle is: {compute_area_circle(number1)}")
