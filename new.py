class Student:
    def__init__(self.name,mark)
    
    self.name=name 
    self.mark=mark
   
    def showdetails(self):
        print(self.name)
        print(self.mark)


s1=Student
s1.showdetails("Ammu",80)
# s1=(self.name="Ammu")
# s1=(self.mark=80)

print(s1)


# class Student:
#     def __init__(self):

#         self.name=("")
#         self.mark=()

# s1=Student()
# s1.name("Ammu")
# s1.mark(80)
# print(s1)



tuple=(1,2,3,4,5)
tuple1=list(tuple)
tuple1.append(6)
list=(tuple1)
print(tuple1)


# array=[1,2,3,4,5]
# a[i]=[0,1,2,3,4]



# rows=1
# i=1
# print(i)
# print(rows,i+1)



class Teacher:
    def __init__(self):
        self.name=name
        self.mark=mark
    def showdetails(name,mark):
        print("my name is",name)


class Student(Teacher):
    def __init__(self):
        super().__init__()

s1=Student()
s1.name=("Ammu")
s1.mark=(80)
