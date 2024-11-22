"""Task 1: Create and Access a Dictionary

#Create a dictionary named book to store the following details:
    title: "The Great Gatsby"
    author: "F. Scott Fitzgerald"
    year_published: 1925"""

#create a simple dictionary   
book = {"title":"The Great Gatsby", "author":"F. Scott Fitzgerald", "year_published": 1925}

#print the dictionary
for key, value in book.items():
    print(f"{key} : {value}")
