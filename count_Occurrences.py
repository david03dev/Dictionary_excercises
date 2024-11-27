""" Task 6: Count Occurrences in a Dictionary
You are given a dictionary representing a group of students and their grades:

grades = {
    "Alice": "A",
    "Bob": "B",
    "Charlie": "A",
    "Diana": "C",
    "Eve": "B",
    "Frank": "A",
    "Grace": "C"
}
1. Write code to count the occurrences of each grade (A, B, C, etc.) and store the results in a new dictionary. ex {"A": 3, "B": 2, "C": 2}  """

grades = {
    "Alice": "A",
    "Bob": "B",
    "Charlie": "A",
    "Diana": "C",
    "Eve": "B",
    "Frank": "A",
    "Grace": "C"
}

# Initialize an empty dictionary to store counts
grade_counts = {}

# Iterate through the grades
for grade in grades.values():
    if grade in grade_counts:
        grade_counts[grade] += 1  # Increment count if grade exists
    else:
        grade_counts[grade] = 1  # Initialize count if grade doesn't exist

# Print the result
print("Grade counts:", grade_counts)



