# class Person:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname

#     def Myfunction(self):
#         print("fname"+"self.lname")

#     def __str__(self):
#         return(f"fname: {self.fname},lname: {self.lname}")
    
# class Student(Person):
#     pass

# p1=Student("Akshara","Manoj")
# print(p1)   


# class Person:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#     def Myfunction(self):
#         print("fname"+self.lname)

#     def __str__(self):
#         return(f"fname: {self.fname}, lname: {self.lname}")
    
# class Student(Person):
#     def __init__(self, fname, lname):
#         super().__init__(fname, lname)
#         self.graduationyear = 2019
    
# p1=Student("ammu","anil")
# print(p1.graduationyear)


# class Teacher:
#     def __init__(self,sub1,sub2,sub3):
#         self.sub1=sub1
#         self.sub2=sub2
#         self.sub3=sub3

#     def Myfunction(self):
#         print("my favourite subject is"+ self.sub)
    
#     def __str__(self):
#         return(f"sub1: {self.sub1},sub2: {self.sub2},sub3: {self.sub3}")

# class Student(Teacher):
#     def __init__(self, sub1, sub2, sub3):
#         super().__init__(sub1, sub2, sub3)
#         self.graduationyear=2019

# p1=Student("dbms","dcf","es")
# print(p1.graduationyear)
# print(p1)   

# class Teacher:
#     def __init__(self,sub1,sub2,sub3):
#         self.sub1=sub1
#         self.sub2=sub2
#         self.sub3=sub3

#     def Myfunction(self):
#         print("my favourite subject is"+ self.sub)
    
#     def __str__(self):
#         return(f"sub1: {self.sub1},sub2: {self.sub2},sub3: {self.sub3}")

# class Student(Teacher):
#     def __init__(self, sub1, sub2, sub3,year):
#         super().__init__(sub1, sub2, sub3)
#         self.graduationyear=year

# p1=Student("dbms","dcf","es",2019)
# print(p1.graduationyear)    


class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place

    def Myfunction(self):
        print("name"+self.age)
    
    def __str__(self):
        return(f"name: {self.name},age: {self.age},place: {self.place}")
    
class Student(Person):
    def __init__(self, name, age, place,year):
        super().__init__(name, age, place)
        self.graduationyear=year

    def welcome(self):
        print("welcome",self.name,self.age,self.place,"to the class of",self.graduationyear)
p1=Student("ammu",25,"kannur",2019)
p1.welcome()
