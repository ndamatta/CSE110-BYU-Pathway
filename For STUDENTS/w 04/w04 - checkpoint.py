# https://byui-cse.github.io/cse110-course/lesson04/checkpoint.html
# 04 Prepare: Checkpoint

#TEMPERATURE CONVERTER
print ("-----TEMPERATURE CONVERTER-----")

user_fahrenheit = int (input ("What is the temperature in Fahrenheit?: "))

celsius = (user_fahrenheit - 32) * 5 / 9

print (f"The temperature in celsius is: {celsius:.1f}ºC")
