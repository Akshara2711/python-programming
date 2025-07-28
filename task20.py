def my_function():
    a=int(input("enter the number"))
    b=int(input("enter the number"))
    operator=input("enter the type of operator (+,-,*,/)")
    result=0
    if operator=="+":
        result=a+b
    elif operator=="-":
        result=a-b
    elif operator=="*":
        result=a*b
    else :
        result=a/b

    print(result)


my_function()





