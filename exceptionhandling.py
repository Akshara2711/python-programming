try:
    print(a)
except NameError:
    print("variable a is not defined")
except IndexError:
    print("index is not defined")
except :
    print("error")
   


try:
    a=5
    print(a)
except NameError:
    print("variable is not defined")
else:
    print("success")
finally:
    print("program completed")



try:
    a=5
    b="4"
    print(a+b)
except NameError:
    print("variable not defined")
except TypeError:
    print("undefined type")