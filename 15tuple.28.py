def second_largest(t):
    unique_elements = list(set(t)) 
    if len(unique_elements) < 2:
        return None 
    return unique_elements[1]

my_tuple = (5, 2, 8, 3, 8)
print(second_largest(my_tuple))
