# https://byui-cse.github.io/cse110-course/lesson03/teach.html
# 03 Teach: Team Activity

print ("----------AREA CALCULATOR----------")

#AREA OF SQUARE
lenght_side_square = float(input("What's the lenght of the side of the square?: "))
area_square = lenght_side_square ** 2
print (f"The area of the square is: {area_square:.2f}")

#AREA OF RECTANGLE
lenght_of_rectangle = float(input("What's the lenght of the rectangle?: "))
width_of_rectangle = float(input("What's the width of the rectangle?: "))
area_rectangle = lenght_of_rectangle * width_of_rectangle
print (f"The area of the rectangle is: {area_square:.2f}")

#AREA OF CIRCLE
radius_of_circle = float(input("What's the radius of the circle?: "))
radius_circle = 3.14 * (radius_of_circle**2)
print (f"The radius of the circle is: {radius_of_circle:.2f}")

import math


