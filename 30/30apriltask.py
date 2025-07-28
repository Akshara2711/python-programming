# fruits=("apple","banana","mango")
# print(fruits)


# fruits=("apple","banana","apple","cheery","banana")
# print(fruits)

# color=("green","red","blue","black")
# print(len(color))

# food=("briyani","icecream","juice","cake")
# print(type(food))

# place=("kannur",)
# print(place)

# home=("A",2,True,"B",4,False)
# print(home)

# school=tuple(("ct","cb","ie","ec"))
# print(school)

# name=("ammu","achu","anu","malu","ponnu","chippi")
# print(name[3])


# course=("java","python","oops","ds","dbms,html")
# y=("css",)
# course+=y
# print(course)

x=("black","blue","green","yellow")
y=list(x)
y[1]="red"
x=tuple(y)
print(x)

fruits=("apple","banana","mango","kiwi")
y=list(fruits)
y.append("orange")
fruits=tuple(y)
print(y)

color=("green","yellow","blue")
(apple,orange,mango)=color
print(apple)
print(orange)
print(mango)