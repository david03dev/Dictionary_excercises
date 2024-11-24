"""Task 2: Add and Update Dictionary Entries

Add a new key-value pair: "genre": "Fiction".
Update the year_published to 1926.
Print the updated dictionary."""

book = {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year_published": 1925}

book["genre"] = "Fiction"
book["year_published"] = 1926

for key, value in book.items():
    print(f"{key:<15}: {value}")
