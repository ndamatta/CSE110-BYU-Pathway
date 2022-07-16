# https://byui-cse.github.io/cse110-course/lesson12/teach.html
# 12 Teach: Team Activity

from posixpath import split


with open("books_and_chapters.txt") as file:

    #---LISTS---
    scriptures = []
    books = []
    chapters = []

    #---VARIABLES---
    largest_number = 0
    largest_name = ""
    largest_scripture = ""

    #---ITERATE FILE---
    for line in file:
        
        stripped_line = line.strip()
        splitted_line = stripped_line.split(":")

        scriptures.append(splitted_line[2])
        books.append(splitted_line[0])
        chapters.append(int(splitted_line[1]))
    
    for i in range(len(chapters)):

        book = books[i]
        chapter = chapters[i]
        scripture = scriptures[i]

        if chapter > largest_number:           
            largest_number = chapter
            largest_name = book
            largest_scripture = scripture

    #---OUTPUT---
    print(f"The largest number of chapters is {largest_number}")
    print(f"The book with the largest number of chapter is {largest_name} with {largest_number}")
