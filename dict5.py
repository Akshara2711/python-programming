
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 88,
    "Ethan": 95
}

top_student = max(students, key=students.get)
top_score = students[top_student]

print(f"The top student is {top_student} with a score of {top_score}.")
