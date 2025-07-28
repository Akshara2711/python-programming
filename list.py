list=['apple','banana','mango']
if 'apple' in list:
    print("yes,'apple' in this list")

name=['appu','ammu','chinnu']
if 'ammu' in name:
    print("yes,'ammu' in this list")

negative=['a','b','c','d','e']
print(negative[-3:-1])


positive=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(positive[1:4])

mylist=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(mylist[3])


change=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
change[1]='black'
print(change)

itemvalue=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
itemvalue[1:3]=["black","white"]
print(itemvalue)

list=["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
list[1:3]=["watermelon"]
print(list)


fruits=["apple", "banana", "cherry", "orange", "kiwi"]
fruits.insert(2,"mango")
print(fruits)

name=["apple", "banana", "cherry", "orange", "kiwi",]
fruits.insert(3,"melon")
print(fruits)

letters=['a','b','c','d','e']
letters.insert(3,'k')
print(letters)

list=['a','b','c']
letter=['d','e','f']
list.extend(letter)
print(list)

fruits=["apple", "banana", "cherry"]
fruits.insert(1,"orange")
print(fruits)

list=["apple", "banana", "cherry"]
list.append("orange")
print(list)

name= ["apple", "banana", "cherry"]
letter=[ "kiwi", "melon", "mango"]
name.extend(letter)
print(name)

list=[ "kiwi", "melon", "mango"]
list.remove("melon")
print(list)

list=[ "kiwi", "melon", "mango"]
list.pop()
print(list)

name=['a','b','c']
del name[0]
print(name)

number=[1,2,3,4]
del number[1]
print(number)

