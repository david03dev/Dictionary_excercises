"""Task 3: Remove and Check Dictionary Entries
Remove the key "genre" from the dictionary.
Check if the key "author" exists in the dictionary.

    Print "Key exists" if it does.
    Otherwise, print "Key does not exist".

Print the final dictionary."""

book = {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year_published": 1926}

# Add a new key-value pair
book["genre"] = "Fiction"

# Remove the key "genre"
del book["genre"]

# Check if "author" exists in the dictionary
if "author" in book.keys():
    print("Key exists")
else:
    print("Key does not exist")

# Print the final dictionary
print(book)
