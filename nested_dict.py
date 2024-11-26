"""Task 5: Nested Dictionaries
You have the following dictionary of employees and their details:
employees = {
    "emp1": {"name": "Alice", "age": 25, "department": "HR"},
    "emp2": {"name": "Bob", "age": 30, "department": "Finance"},
    "emp3": {"name": "Charlie", "age": 28, "department": "IT"}
}
Write code to:
1.Print each employee's name and department in the format:

Alice works in HR
Bob works in Finance
Charlie works in IT

2.Add a new key-value pair "salary": 50000 to each employee's details.
3.Print the updated dictionary.  """

employees = {
    "emp1": {"name": "Alice", "age": 25, "department": "HR"},
    "emp2": {"name": "Bob", "age": 30, "department": "Finance"},
    "emp3": {"name": "Charlie", "age": 28, "department": "IT"}
}

# Print name and department
for emp_id, details in employees.items():
    print(f"{details['name']} works in {details['department']}")

# Add salary key to each employee
for emp_id, details in employees.items():
    details["salary"] = 50000

# Print the updated dictionary
print("\nUpdated Employees Dictionary:")
for emp_id, details in employees.items():
    print(f"{emp_id}: {details}")
