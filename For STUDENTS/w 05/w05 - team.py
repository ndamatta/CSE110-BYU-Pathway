# https://byui-cse.github.io/cse110-course/lesson05/teach.html
# 05 Teach: Team Activity
# Note: I was testing some Tkinter here, that's not required. Just read what's inside of the function
from tkinter import *

root = Tk()
root.geometry("400x200")
root.config(bg = "lightgray")
root.title("GRADE CHECKER")

grade = 0
screen_text = IntVar()

def grade_check():

    global grade

    grade = screen_text.get()

    if grade <=0 or grade >100:
        LabelResult.config(text = "Invalid grade!", fg = "red")
    
    elif grade >= 90:
        LabelResult.config(text = "Your grade is: A", fg = "green")

    elif grade >= 80:
        LabelResult.config(text = "Your grade is: B", fg = "yellow")

    elif grade >= 70:
        LabelResult.config(text = "Your grade is: C", fg = "lightgreen")

    elif grade >= 60:
        LabelResult.config(text = "Your grade is: D", fg = "lighred")

    elif grade >= 60:
        LabelResult.config(text = "Your grade is: F", fg = "red")

    elif grade < 60:
        LabelResult.config(text = "Your grade is too low!", fg = "red")
    
    grade = screen_text.set(0)

myFrame = Frame(root)
myFrame.config(bg = "lightgray")
myFrame.pack()

Label_Title = Label(myFrame, text = "GRADE CHECKER", font = ("TimesNewRoman, 10"))
Label_Title.grid(row = 1, columnspan = 5, pady = 10)

myEntry = Entry(myFrame, textvariable = screen_text)
myEntry.grid(row = 3, column = 3, padx = 10)
myEntry.config(justify = "center")

myLabel = Label(myFrame, text = "Insert your calification: ")
myLabel.grid(row = 3, column = 2, padx = 4)

LabelResult = Label(myFrame)
LabelResult.grid(row = 6, column = 3)

myButton = Button(myFrame, text = "Check", command = grade_check)
myButton.grid(row = 5, column = 3, pady = "7")


root.mainloop()
