"""Task 4: Iterate Over a Dictionary
students = {"Alice": 85, "Bob": 90, "Charlie": 78, "Diana": 92}
Write a loop to iterate over the dictionary and print each student's name and score in the format:
Alice scored 85
Bob scored 90
Charlie scored 78
Diana scored 92
"""

students = {"Alice": 85, "Bob": 90, "Charlie": 78, "Diana": 92}

# Initialize total score
total_score = 0

# Loop through students and scores
for student, score in students.items():
    print(f"{student} scored {score}")
    total_score += score

# Calculate average
average_score = total_score / len(students)
print(f"Average score is {average_score:.2f}")
