# https://byui-cse.github.io/cse110-course/lesson04/teach.html 
# 04 Teach: Team Activity
import math
#formula:  v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)t))

print ("-----VELOCITY CALCULATOR-----")
print ("Welcome to the velocity calculator. Please enter the following:\n")

#VARIABLES AND INPUTS
m = float(input("Mass (in kg): "))
g = float(input("Aceleration due to gravity (9.8 m/s^2 on Earth, 24 m/s^2 on Jupiter): "))
t = float(input("Time (in seconds): "))
p = float(input("Density of fluid (1.3 kg/m^3 for air, 1000 kg/m^3 for water): "))
A = float(input("Cross sectional area of projectile (in square meters): "))
C = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

#CALCULATION 1: c = (1/2) * p * A * C
c = (1 / 2) * p * A * C

#CALCULATION 2: v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)t))
velocity = math.sqrt(m * g / c)  * (1 - math.exp(( - math.sqrt(m * g * c) / m) * t))

#OUTPUT
print () #blank line
print (f"The inner value of c is: {c:.3f}")
print (f"The velocity after {t} seconds is: {velocity:.3f} m/s")
