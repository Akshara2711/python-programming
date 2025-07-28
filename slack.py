# name = input("Enter your name: ")
# print(f"Hello, {name}! Nice to meet you.")

# number = int(input("Enter a number: "))

# if number % 2 == 0:
#     print(f"{number} is even.")
# else:
#     print(f"{number} is odd.")

# numbers = [10, 20, 30, 40, 50]

# for number in numbers:
#     print(number)

# def square(number):
#     return number ** 2

# result = square(5)
# print("Square:", result)

# text = "internship"
# reversed_text = text[::-1]
# print("Reversed string:", reversed_text)

# # Convert number to string
# num = 123
# num_str = str(num)
# print("Value:", num_str)
# print("Type after conversion to string:", type(num_str))

# # Convert string to number
# str_num = "456"
# str_to_num = int(str_num)
# print("Value:", str_to_num)
# print("Type after conversion to integer:", type(str_to_num))

# person = {
#     "name": "Alice",
#     "age": 25,
#     "city": "New York"
# }


# print("Name:", person["name"])
# print("Age:", person["age"])
# print("City:", person["city"])

# for i in range(1, 21):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# def add_numbers():
#     try:
#         num1 = float(input("Enter the first number: "))
#         num2 = float(input("Enter the second number: "))
#         result = num1 + num2
#         print("Sum:", result)
#     except ValueError:
#         print("Invalid input. Please enter numeric values.")


# add_numbers()

# sentence = input("Enter a sentence: ")

# words = sentence.split()

# for word in words:
#     print(word)

# def factorial(n):
#     if n == 0 or n == 1:  
#         return 1
#     else:
#         return n * factorial(n - 1)

# def is_palindrome(s):
    
#     s = s.replace(" ", "").lower()
   
#     return s == s[::-1]

# print(is_palindrome("madam"))  
# print(is_palindrome("racecar")) 
# print(is_palindrome("hello"))  

# def filter_even_numbers(numbers):
#     return [num for num in numbers if num % 2 == 0]


# nums = [1, 2, 3, 4, 5, 6]
# print(filter_even_numbers(nums))  

# def triangle_area(base, height):
#     return 0.5 * base * height

# print(triangle_area(5, 10))  


# students = {
#     "Alice": 85,
#     "Bob": 92,
#     "Charlie": 78,
# }

# for name, marks in students.items():
#     print(f"{name}: {marks}")

# sum_of_squares = sum(i**2 for i in range(1, 11))

# print(sum_of_squares) 

# def safe_divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return "Error: Cannot divide by zero."


# print(safe_divide(10, 2))  
# print(safe_divide(10, 0)) 

# def char_count(s):
#     counts = {}
#     for char in s:
#         counts[char] = counts.get(char, 0) + 1
#     return counts


# result = char_count("hello world")
# print(result)

# my_list = [1, 2, 3, 4, 5]
# reversed_list = my_list[::-1]
# print(reversed_list)  

# def contains_intern(s):
#     return "intern" in s


# print(contains_intern("I am an intern"))  
# print(contains_intern("Hello world"))     


# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)

# print(factorial(5))  


# def is_palindrome(s):
#     return s == s[::-1]

# print(is_palindrome("madam"))  

# def is_palindrome(s):
#     return s == s[::-1]

# print(is_palindrome("madam"))

# def triangle_area(base, height):
#     return 0.5 * base * height

# print(triangle_area(10, 5)) 

# students = {
#     "Alice": 85,
#     "Bob": 92,
#     "Charlie": 78
# }

# for name, marks in students.items():
#     print(f"{name}: {marks}")

# sum_of_squares = sum(i**2 for i in range(1, 11))
# print(sum_of_squares) 

# def safe_divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return "Cannot divide by zero"

# print(safe_divide(10, 2)) 
# print(safe_divide(10, 0))  


# from collections import Counter

# def count_characters(s):
#     return dict(Counter(s))

# print(count_characters("hello world"))

# my_list = [1, 2, 3, 4, 5]
# reversed_list = my_list[::-1]
# print(reversed_list)  

# let myList = [1, 2, 3, 4, 5];
# myList.reverse();
# console.log(myList); 




# def contains_intern(s):
#     return "intern" in s.lower()

# print(contains_intern("The intern is here."))  
# print(contains_intern("No internship today.")) 
# print(contains_intern("External project."))     


# def manual_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr

# print(manual_sort([5, 2, 9, 1, 5, 6]))  


# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True

# print(is_prime(7))  
# print(is_prime(10)) 

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# for row in matrix:
#     for elem in row:
#         print(elem, end=' ')
#     print()

# for i in range(1, 51):
#     if i % 3 == 0 or i % 5 == 0:
#         print(i, end=' ')



# def get_initials(name):
#     parts = name.split()
#     initials = '.'.join([p[0].upper() for p in parts])
#     return initials + '.'

# print(get_initials("John Doe")) 

# def rotate_right(arr, k=2):
#     n = len(arr)
#     k = k % n 
#     return arr[-k:] + arr[:-k]

# print(rotate_right([1, 2, 3, 4, 5])) 


# product = {
#     "name": "Laptop",
#     "price": 1000,
#     "brand": "TechBrand"
# }

# def update_price(prod, new_price):
#     prod["price"] = new_price

# update_price(product, 1200)
# print(product) 


# def is_leap_year(year):
#     return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# print(is_leap_year(2024))  
# print(is_leap_year(1900)) 


# def count_chars(s):
#     upper = lower = digit = 0
#     for char in s:
#         if char.isupper():
#             upper += 1
#         elif char.islower():
#             lower += 1
#         elif char.isdigit():
#             digit += 1
#     return upper, lower, digit

# print(count_chars("Hello123World"))


# def print_triangle(rows):
#     for i in range(1, rows + 1):
#         print('* ' * i)

# print_triangle(5)


# import random

# def atm():
#     balance = 1000 
#     while True:
#         print("\nATM Menu:\n1. Check Balance\n2. Withdraw\n3. Deposit\n4. Exit")
#         choice = input("Enter your choice: ")
#         if choice == '1':
#             print("Balance:", balance)
#         elif choice == '2':
#             amount = float(input("Enter amount to withdraw: "))
#             if amount > balance:
#                 print("Insufficient funds.")
#             else:
#                 balance -= amount
#                 print("Withdrawn:", amount)
#         elif choice == '3':
#             amount = float(input("Enter amount to deposit: "))
#             balance += amount
#             print("Deposited:", amount)
#         elif choice == '4':
#             print("Thank you for using the ATM.")
#             break
#         else:
#             print("Invalid choice.")


# def binary_to_decimal(binary_str):
#     return int(binary_str, 2)

# def decimal_to_binary(decimal_num):
#     return bin(decimal_num)[2:]


# def count_frequency(lst):
#     freq = {}
#     for num in lst:
#         freq[num] = freq.get(num, 0) + 1
#     return freq


# def average_of_randoms():
#     nums = [random.randint(1, 50) for _ in range(5)]
#     avg = sum(nums) / len(nums)
#     return nums, avg


# def categorize_number(n):
#     if n < 10:
#         return "Small"
#     elif 10 <= n <= 100:
#         return "Medium"
#     else:
#         return "Large"


# def replace_spaces(s):
#     return s.replace(' ', '_')


# def list_intersection(lst1, lst2):
#     return list(set(lst1) & set(lst2))


# def is_alpha_only(s):
#     return s.isalpha()

# def safe_string_to_int(s):
#     try:
#         return int(s)
#     except ValueError:
#         return "Invalid Input"

# def count_words_starting_with_vowel(sentence):
#     vowels = 'aeiouAEIOU'
#     words = sentence.split()
#     return sum(1 for word in words if word and word[0] in vowels)





# def is_valid_password(password):
#     return (
#         len(password) >= 8 and
#         any(char.isdigit() for char in password) and
#         any(char.isupper() for char in password)
#     )

# print(is_valid_password("Password1"))  

# data = {
#     "user": {
#         "name": "Alice",
#         "address": {
#             "city": "New York",
#             "zip": "10001"
#         }
#     }
# }

# print(data["user"]["address"]["city"])  


# def get_primes(n):
#     primes = []
#     for num in range(2, n+1):
#         if all(num % i != 0 for i in range(2, int(num**0.5)+1)):
#             primes.append(num)
#     return primes

# print(get_primes(100))


# from datetime import datetime

# now = datetime.now()
# print(now.strftime("%Y-%m-%d %H:%M:%S"))


# n = 3
# num = 1
# for i in range(1, n+2):
#     for j in range(i):
#         print(num, end=" ")
#         num += 1
#     print()


# words = ["banana", "apple", "cherry"]
# words.sort()
# print(words)  

# def convertTemp(temp, unit):
#     if unit == "C":
#         return temp * 9/5 + 32
#     elif unit == "F":
#         return (temp - 32) * 5/9
#     else:
#         return "Invalid unit"

# print(convertTemp(100, "C"))  
# print(convertTemp(212, "F"))  


# words = ["level", "world", "radar", "python"]
# palindromes = [word for word in words if word == word[::-1]]
# print(palindromes) 

# def has_unique_digits(n):
#     digits = str(n)
#     return len(set(digits)) == len(digits)

# print(has_unique_digits(1234)) 
# print(has_unique_digits(1123))  

# sentence = "Hello world from Python"
# words = sentence.split()
# reversed_words = [word[::-1] for word in words]
# print(reversed_words) 


# from collections import Counter

# def count_digits(n):
#     return dict(Counter(str(n)))

# print(count_digits(1123581122))  

# import re

# def capitalize_sentences(paragraph):
#     sentences = re.split(r'(?<=[.!?])\s+', paragraph)
#     return ' '.join(s.capitalize() for s in sentences)

# text = "hello. how are you? i'm fine!"
# print(capitalize_sentences(text))

# def arrays_equal(arr1, arr2):
#     return arr1 == arr2

# print(arrays_equal([1, 2, 3], [1, 2, 3]))  
# print(arrays_equal([1, 2], [2, 1]))        

# def clean_dict(d):
#     return {k: v for k, v in d.items() if v not in (None, '')}

# data = {'a': 1, 'b': '', 'c': None, 'd': 4}
# print(clean_dict(data)) 


# def outer(add_val):
#     def inner(x):
#         return x**2 + add_val
#     return inner

# f = outer(5)
# print(f(3))  


# def recursive_sum(lst):
#     if not lst:
#         return 0
#     return lst[0] + recursive_sum(lst[1:])

# print(recursive_sum([1, 2, 3, 4]))  

# def all_unique(s):
#     return len(set(s)) == len(s)

# print(all_unique("abcde"))  
# print(all_unique("hello"))  

# def is_prime(n):
#     return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5)+1))

# print(sum(i for i in range(1, 101) if is_prime(i)))  
# import re

# def remove_special_chars(s):
#     return re.sub(r'[^a-zA-Z0-9\s]', '', s)

# print(remove_special_chars("Hello@# World!123"))  
# def is_valid_mobile(num):
#     return isinstance(num, str) and num.isdigit() and len(num) == 10

# print(is_valid_mobile("9876543210")) 
# print(is_valid_mobile("1234abc890")) 




# def find_index(lst, number):
#     try:
#         return lst.index(number)
#     except ValueError:
#         return -1  

# def sort_by_length(strings):
#     return sorted(strings, key=len)

# def swap_case(s):
#     return s.swapcase()


# class ShoppingCart:
#     def __init__(self):
#         self.items = {}

#     def add(self, item, price):
#         self.items[item] = self.items.get(item, 0) + price

#     def remove(self, item):
#         if item in self.items:
#             del self.items[item]

#     def total(self):
#         return sum(self.items.values())

# def to_title_case(sentence):
#     return sentence.title()

# def print_dict(d):
#     for key, value in d.items():
#         print(f"{key}: {value}")

# def sum_digits(s):
#     return sum(int(char) for char in s if char.isdigit())


# def count_passed(marks):
#     return sum(1 for mark in marks if mark >= 40)


# def double(n):
#     return n * 2

# def add_five(n):
#     return n + 5

# def chained_function(n):
#     return add_five(double(n))


# def get_number_input(prompt="Enter a number: "):
#     try:
#         return int(input(prompt))
#     except ValueError:
#         print("Invalid input! Please enter a valid number.")
#         return None


# from collections import Counter

# paragraph = "This is a test. This test is only a test."
# words = paragraph.lower().replace('.', '').split()
# word_freq = Counter(words)
# print(word_freq)


# numbers = [1, 2, 3, 4, 5, 6, 7]
# even = [n for n in numbers if n % 2 == 0]
# odd = [n for n in numbers if n % 2 != 0]
# print("Even:", even)
# print("Odd:", odd)


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# transpose = list(map(list, zip(*matrix)))
# print(transpose)

# data = {'apple': 10, 'banana': 5, 'cherry': 20}
# sorted_dict = dict(sorted(data.items(), key=lambda item: item[1]))
# print(sorted_dict)

# nums = [10, -3, 4, -1, 0, -7, 8]
# negatives = [n for n in nums if n < 0]
# print(negatives)


# def power(base, exp):
#     result = 1
#     for _ in range(abs(exp)):
#         result *= base
#     return result if exp >= 0 else 1 / result

# print(power(2, 3))  
# print(power(2, -2))  

# temps = [float(input(f"Enter temperature {i+1}: ")) for i in range(5)]
# print("Average:", sum(temps)/len(temps))
# print("Max:", max(temps))
# print("Min:", min(temps))


# keys = ['a', 'b', 'c']
# values = [1, 2, 3]
# combined = dict(zip(keys, values))
# print(combined)

# nums = [1, 2, 3, 4]
# result = ''.join(map(str, nums))
# print(result)


# from datetime import datetime, timedelta

# for i in range(6):
#     day = datetime.now() + timedelta(days=i)
#     print(day.strftime("%A"))

# def reverse_string(s):
#     if len(s) == 0:
#         return ""
#     return reverse_string(s[1:]) + s[0]

# print(reverse_string("hello"))

# def print_pyramid(rows):
#     for i in range(rows):
#         spaces = ' ' * (rows - i - 1)
#         stars = '*' * (2 * i + 1)
#         print(spaces + stars)

# print_pyramid(3)

# a = [1, 2, 3, 4]
# b = [3, 4, 5, 6]

# diff_a = [x for x in a if x not in b]
# diff_b = [x for x in b if x not in a]

# print("In a not in b:", diff_a)
# print("In b not in a:", diff_b)

# def is_armstrong(n):
#     digits = str(n)
#     power = len(digits)
#     return sum(int(d)**power for d in digits) == n

# print(is_armstrong(153))  
# print(is_armstrong(123))  

# sentence = "This is a simple sentence."
# word_count = len(sentence.split())
# print("Word count:", word_count)


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [0, 1, 2]
# ]

# max_row = max(matrix, key=sum)
# print("Row with max sum:", max_row)


# import time

# for _ in range(5):
#     print(time.strftime("%H:%M:%S"), end='\r')
#     time.sleep(1)


# user_profile = {
#     "name": "Alice",
#     "address": {
#         "street": "123 Main St",
#         "city": "Wonderland"
#     },
#     "marks": {
#         "math": 95,
#         "science": 88
#     }
# }

# print(user_profile)


# words = ["hello", "world"]
# uppercase_words = [w.upper() for w in words]
# # OR using map:
# # uppercase_words = list(map(str.upper, words))
# print(uppercase_words)


# nums = [5, 9, 3, 12, 7, 18, 2]
# sorted_nums = sorted(nums)
# div_by_3 = [n for n in sorted_nums if n % 3 == 0]
# print("Sorted:", sorted_nums)
# print("Divisible by 3:", div_by_3)


