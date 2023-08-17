# https://byui-cse.github.io/cse110-course/lesson02/teach.html
# 02 Teach: Programming Activity

from dataclasses import asdict
from distutils.command.build_scripts import first_line_re
from statistics import harmonic_mean

#USER INPUT
print ("Please enter the following information: ")
first_name = input ("First name?: ")
last_name = input ("Second name?: ")
email = input ("Email?: ")
phone_number = input ("Phone number?: ")
job_title = input ("Job title?: ")
id_number = input ("ID number?: ")

#ADDITIONAL INFO
hair_color = input ("Hair color: ")
eyes_color = input ("Eyes color: ")
month = input ("Starting Month: ")
training = input ("Completed additional training? ")

#OUTPUT
print ("n\Your ID Card is: ")
print ("----------------------------------------")
print (f"{last_name.upper()}, {first_name.capitalize()}")
print (f"{job_title.title()}")
print (f"ID Number: {id_number}")
print ()
print (f"{email.lower()}")
print (f"{phone_number}")
print ()
print (f"Hair: {hair_color:15} Eyes: {eyes_color}")
print (f"Month: {month:14} Training: {training}")
print ("----------------------------------------")

