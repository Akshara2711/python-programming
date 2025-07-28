original_dict = {1: 'a', 2: 'b', 3: 'c'}


inverted_dict = {value: key for key, value in original_dict.items()}

print(inverted_dict)
