def calculator(x,y,operation):
    if operation=="add":
        return x+y
    elif operation=="substration":
        return x-y
    elif operation=="multiplication":
        return x*y
    elif operation=="division":
        return x/y
    elif operation=="modules":
        return x%y
    elif operation=="Exponentiation":
        return x**y
    elif operation=="Floor division":
        return x//y
    else:
        return "invalid operator"

print("Addition:", calculator(5, 2, "add"))
print("Subtraction:", calculator(5, 2, "substration"))
print("Multiplication:", calculator(5, 2, "multiplication"))
print("Division:", calculator(5, 2, "division"))
print("modules:",calculator(5,2,"modules"))
print("Exponentiation:",calculator(5,2,"Exponentiation"))
print("Floor division:",calculator(5,2,"Floor division"))


