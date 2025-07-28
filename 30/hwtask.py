# def print_sum(a, b):
#     sum_result = a + b
#     print("The sum is:", sum_result)

# print_sum(5, 7)
     

# def concatenate_strings(str1, str2):
#     result = str1 + str2
#     print("Concatenated string:", result)


# concatenate_strings("Hello, ", "world!")

# def loop_through_range(start, end):
#     for i in range(start, end):
#         print(i)


# loop_through_range(1, 6)

# def check_even_odd(num):
#     if num % 2 == 0:
#         print(f"{num} is even.")
#     else:
#         print(f"{num} is odd.")


# check_even_odd(7)
# check_even_odd(10)

# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result


# print("Factorial of 5 is:", factorial(5))

# 
# def calculator(a, b, operation):
#     if operation == "add":
#         return a + b
#     elif operation == "subtract":
#         return a - b
#     elif operation == "multiply":
#         return a * b
#     elif operation == "divide":
#         if b != 0:
#             return a / b
#         else:
#             return "Error: Division by zero"
#     else:
#         return "Invalid operation"


# print("Addition:", calculator(10, 5, "add"))
# print("Subtraction:", calculator(10, 5, "subtract"))
# print("Multiplication:", calculator(10, 5, "multiply"))
# print("Division:", calculator(10, 5, "divide"))
    

# fruits = {"apple", "banana", "orange", "grape", "mango"}
# print("Set of fruits:", fruits)
   

# fruits = {"apple", "banana", "orange", "grape", "mango"}
# fruits.add("pineapple")
# print("Updated set of fruits:", fruits)
             

# fruits = {"apple", "banana", "orange", "grape", "mango", "pineapple"}
# fruits.remove("banana")
# print("Updated set of fruits:", fruits)
    

# fruits = {"apple", "orange", "grape", "pineapple", "mango"}

# if "apple" in fruits:
#     print("Apple is in the set.")
# else:
#     print("Apple is not in the set.")   


# def remove_duplicates(lst):
#     return list(set(lst))


# my_list = [1, 2, 3, 4, 5, 2, 3, 6, 1]
# unique_list = remove_duplicates(my_list)
# print("List after removing duplicates:", unique_list)
     

# fruits = {"apple", "banana", "orange", "grape", "mango"}

# fruits.clear()

# print("Set after clearing:", fruits)
   


# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print(f"{num} is even.")
# else:
#     print(f"{num} is odd.")
       

# num = float(input("Enter a number: "))

# if num > 0:
#     print(f"{num} is positive.")
# elif num < 0:
#     print(f"{num} is negative.")
# else:
#     print(f"{num} is zero.")
     


# age = int(input("Enter your age: "))

# if age >= 18:
#     print("Eligible to vote")
# else:
#     print("Not eligible to vote")
    

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))

# largest = max(num1, num2, num3)
# print(f"The largest number is: {largest}")
    

# score = float(input("Enter the student's score: "))

# if score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >= 70:
#     grade = "C"
# elif score >= 60:
#     grade = "D"
# else:
#     grade = "F"

# print(f"The student's grade is: {grade}")
    

# students_marks = {
#     "Alice": 85,
#     "Bob": 92,
#     "Charlie": 78,
#     "David": 88,
#     "Eva": 95
# }

# for student, marks in students_marks.items():
#     print(f"{student}: {marks}")
    

# def count_character_frequency(input_string):
    
#     char_frequency = {}

#     for char in input_string:
        
#         if char in char_frequency:
#             char_frequency[char] += 1
        
#         else:
#             char_frequency[char] = 1

    
#     for char, frequency in char_frequency.items():
#         print(f"'{char}': {frequency}")


# input_string = "hello world"
# count_character_frequency(input_string)
   

# def check_and_add_key(my_dict, key, default_value):
    
#     if key not in my_dict:
#         my_dict[key] = default_value
#         print(f"Key '{key}' was not found. Added with default value: {default_value}")
#     else:
#         print(f"Key '{key}' already exists with value: {my_dict[key]}")


# my_dict = {"name": "Alice", "age": 25}

# check_and_add_key(my_dict, "age", 30) 
# check_and_add_key(my_dict, "city", "New York")  
    

# def merge_dicts(dict1, dict2):
   
#     merged_dict = dict1.copy()  
#     merged_dict.update(dict2) 
#     return merged_dict

# dict1 = {"name": "Alice", "age": 25}
# dict2 = {"city": "New York", "occupation": "Engineer"}

# merged_dict = merge_dicts(dict1, dict2)
# print("Merged Dictionary:", merged_dict)
   

# def find_top_student(students_scores):
#     top_student = max(students_scores, key=students_scores.get)
#     top_score = students_scores[top_student]
    
#     return top_student, top_score

# students_scores = {
#     "Alice": 85,
#     "Bob": 92,
#     "Charlie": 78,
#     "David": 88,
#     "Eva": 95
# }

# top_student, top_score = find_top_student(students_scores)
# print(f"The student with the highest marks is {top_student} with a score of {top_score}.")
   

# def sort_dict_by_value(my_dict, ascending=True):
  
#     sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=not ascending))
#     return sorted_dict

# students_scores = {
#     "Alice": 85,
#     "Bob": 92,
#     "Charlie": 78,
#     "David": 88,
#     "Eva": 95
# }

# ascending_sorted = sort_dict_by_value(students_scores, ascending=True)
# print("Sorted by values (ascending):", ascending_sorted)


# descending_sorted = sort_dict_by_value(students_scores, ascending=False)
# print("Sorted by values (descending):", descending_sorted)
    

# def invert_dict(my_dict):

#     inverted_dict = {v: k for k, v in my_dict.items()}
#     return inverted_dict


# original_dict = {1: 'a', 2: 'b'}
# inverted_dict = invert_dict(original_dict)
# print("Inverted Dictionary:", inverted_dict)
   

# def sort_dict_by_value(my_dict, ascending=True):
    
#     sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=not ascending))
#     return sorted_dict

# students_scores = {
#     "Alice": 85,
#     "Bob": 92,
#     "Charlie": 78,
#     "David": 88,
#     "Eva": 95
# }


# ascending_sorted = sort_dict_by_value(students_scores, ascending=True)
# print("Sorted by values (ascending):", ascending_sorted)

# descending_sorted = sort_dict_by_value(students_scores, ascending=False)
# print("Sorted by values (descending):", descending_sorted)
   
# def sum_dict_values(my_dict):
   
#     total_sum = sum(my_dict.values())
#     return total_sum

# students_scores = {
#     "Alice": 85,
#     "Bob": 92,
#     "Charlie": 78,
#     "David": 88,
#     "Eva": 95
# }

# total = sum_dict_values(students_scores)
# print("Sum of all values:", total)
   

# def remove_low_values(my_dict, threshold=50):
    
#     filtered_dict = {k: v for k, v in my_dict.items() if v >= threshold}
#     return filtered_dict


# students_scores = {
#     "Alice": 85,
#     "Bob": 92,
#     "Charlie": 45,
#     "David": 88,
#     "Eva": 30
# }
# filtered_scores = remove_low_values(students_scores, threshold=50)
# print("Filtered Dictionary:", filtered_scores)
   

# def lists_to_dict(keys, values):
    
#     result_dict = dict(zip(keys, values))
#     return result_dict

# keys = ["name", "age", "city"]
# values = ["Alice", 25, "New York"]

# result = lists_to_dict(keys, values)
# print("Converted Dictionary:", result)
   

