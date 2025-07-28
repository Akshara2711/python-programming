scores = {
    "Alice": 85,
    "Bob": 42,
    "Charlie": 78,
    "Diana": 33,
    "Ethan": 95
}
filtered_scores = {key: value for key, value in scores.items() if value >= 50}
print("Filtered scores:", filtered_scores)
