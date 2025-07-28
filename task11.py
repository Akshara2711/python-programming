# num = 0
# factorial = 1

# if num < 0:
#    print("must be positive")
# elif num == 0:
#    print("factorial = 1")
# else:
#    for i in range(1,num + 1):
#        factorial = factorial*i
#    print(num, factorial)

num=6
result=1
while num>0:
    result*=num
    num-=1
   
print(result)
