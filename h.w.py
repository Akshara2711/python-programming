# import re
# from collections import Counter

# def most_frequent_word(paragraph):
#     words = re.findall(r'\w+', paragraph.lower())
#     if not words:
#         print("No words found.")
#         return

#     freq = Counter(words)
#     most_common = freq.most_common(1)[0]  # (word, count)

#     print(f"Most frequent word: {most_common[0]} ({most_common[1]} times)")

# # Example usage:
# most_frequent_word("Hello world! Hello everyone. This world is beautiful.")


# def hotel_booking(days, room_type):
#     prices = {'standard': 1000, 'deluxe': 2000, 'suite': 3000}
#     price_per_day = prices.get(room_type.lower(), 0)
#     total = days * price_per_day
#     print(f"Room Type: {room_type}, Days: {days}, Total Bill: ₹{total}")

# hotel_booking(3, 'Deluxe')

# def diagonal_traverse(matrix):
#     if not matrix: return
#     rows, cols = len(matrix), len(matrix[0])
#     result = []
#     for d in range(rows + cols - 1):
#         intermediate = []
#         r = 0 if d < cols else d - cols + 1
#         c = d if d < cols else cols - 1
#         while r < rows and c > -1:
#             intermediate.append(matrix[r][c])
#             r += 1
#             c -= 1
#         if d % 2 == 0:
#             result.extend(intermediate[::-1])
#         else:
#             result.extend(intermediate)
#     print(result)

# diagonal_traverse([[1,2,3],[4,5,6],[7,8,9]])


# def currency_convert(amount, from_currency):
#     rates = {'INR': 1, 'USD': 83, 'EUR': 90}
#     if from_currency not in rates:
#         print("Unknown currency")
#         return
#     for to_currency, rate in rates.items():
#         if to_currency != from_currency:
#             converted = (amount / rates[to_currency] * rates[from_currency])
#             print(f"{amount} {from_currency} = {converted:.2f} {to_currency}")

# currency_convert(1000, 'INR')
# currency_convert(10, 'USD')


# def authenticate(email, password):
#     stored = {'email': 'user@example.com', 'password': 'secret123'}
#     if email == stored['email'] and password == stored['password']:
#         print("Login successful")
#     else:
#         print("Invalid credentials")

# authenticate('user@example.com', 'secret123')


# def write_file(content, filename="sample.txt"):
#     with open(filename, "w") as f:
#         f.write(content)

# def read_file(filename="sample.txt"):
#     with open(filename, "r") as f:
#         print("File content:", f.read())

# write_file("This is a test.")
# read_file()


# def has_substring(sentence, sub):
#     for i in range(len(sentence) - len(sub) + 1):
#         if sentence[i:i+len(sub)] == sub:
#             print("Substring found")
#             return True
#     print("Substring not found")
#     return False

# has_substring("Python is great", "is")


# def highest_scorer(grades):
#     if not grades:
#         print("No students.")
#         return
#     top_student = max(grades, key=grades.get)
#     print(f"Top student: {top_student} ({grades[top_student]})")

# highest_scorer({'Alice': 85, 'Bob': 92, 'Charlie': 88})


# def print_numeric_props(obj):
#     for key, value in obj.items():
#         if isinstance(value, (int, float)):
#             print(f"{key}: {value}")

# print_numeric_props({'name': 'John', 'age': 30, 'score': 88, 'passed': True})


# def ticket_price(age):
#     if age < 12:
#         print("₹20 (Child)")
#     elif age < 60:
#         print("₹50 (Adult)")
#     else:
#         print("₹30 (Senior)")

# ticket_price(65)



# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(7))  


# def remove_vowels(sentence):
#     vowels = "aeiouAEIOU"
#     result = ''.join([c for c in sentence if c not in vowels])
#     print(result)

# remove_vowels("This is a sample sentence.")


# user = {
#     'name': 'Alice',
#     'profile': {
#         'address': {
#             'city': 'New York',
#             'zip': '10001'
#         },
#         'age': 30
#     }
# }

# print("City:", user['profile']['address']['city'])  


# def above_average(numbers):
#     avg = sum(numbers) / len(numbers)
#     result = [num for num in numbers if num > avg]
#     print("Above average numbers:", result)

# above_average([10, 20, 30, 40, 50])


# students = [
#     {'name': 'Alice', 'marks': 85},
#     {'name': 'Bob', 'marks': 72},
#     {'name': 'Charlie', 'marks': 91}
# ]

# sorted_students = sorted(students, key=lambda s: s['marks'], reverse=True)
# for student in sorted_students:
#     print(f"{student['name']} - {student['marks']}")


# def vending_machine(balance):
#     items = {'Chips': 20, 'Soda': 35, 'Candy': 10}
#     print("Available items:")
#     for item, price in items.items():
#         print(f"{item}: ₹{price}")

#     choice = input("Choose an item: ")
#     price = items.get(choice)

#     if price is None:
#         print("Invalid item.")
#     elif balance < price:
#         print("Insufficient balance.")
#     else:
#         balance -= price
#         print(f"Dispensing {choice}. Remaining balance: ₹{balance}")



# count = len([n for n in range(1, 101) if n % 3 == 0 and n % 7 == 0])
# print("Count:", count)

