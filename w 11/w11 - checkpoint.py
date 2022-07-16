# https://byui-cse.github.io/cse110-course/lesson11/checkpoint.html
# 11 Prepare: Checkpoint

with open("books.txt") as books:

    for book in books:
        
        books_striped = book.strip()

        print(books_striped)