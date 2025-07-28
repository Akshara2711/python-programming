students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 88,
    "Ethan": 95
}
sorted_asc = dict(sorted(students.items(), key=lambda item: item[1]))
print("Ascending order:", sorted_asc)

sorted_desc = dict(sorted(students.items(), key=lambda item: item[1], reverse=True))
print("Descending order:", sorted_desc)
