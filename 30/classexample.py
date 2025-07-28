# class Student:
#     x=5

# p1=Student()
# print(p1.x)

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# p1=Person("ammu",20)
# print(p1.name)
# print(p1.age)  

# class Student:
#     def __init__(self,name,mark,age,place):
#         self.name=name
#         self.mark=mark
#         self.age=age
#         self.place=place






# p1=Student("ammu",70,20,"kannur")
# p2=Student ("achu",95,20,"edakkad")
# p3=Student("anju",80,20,"kozhikod")
# p4=Student("jithu",95,20,"kannur")
# p5=Student("appu",65,20,"ezhilodu")
# p6=Student("anu",60,20,"kannur")

# print(f"Name: {p1.name}, Marks: {p1.mark}, Age: {p1.age}, Place: {p1.place}")
# print(f"Name: {p2.name}, marks: {p2.mark},Age: {p2.age},place: {p2.place}")
# print(f"Name: {p3.name}, Marks: {p3.mark}, Age: {p3.age}, Place: {p3.place}")
# print(f"Name: {p4.name}, Marks: {p4.mark}, Age: {p4.age}, Place: {p4.place}")
# print(f"Name: {p5.name}, Marks: {p5.mark}, Age: {p5.age}, Place: {p5.place}")
# print(f"Name: {p6.name}, Marks: {p6.mark}, Age: {p6.age}, Place: {p6.place}")


# class Place:
#     def __init__(self,name,district,pincode,lanmark):
#         self.name=name
#         self.district=district
#         self.pincode=pincode
#         self.landmark=lanmark

# p1=Place("edakkad","Kannur",670663,"abc")
# p2=Place("ezhilodu","kannur",654837,"abc")
# p3=Place("kadambur","Kannur",670663,"abc")
# p4=Place("chandera","Kasargod",876543,"abc")
# p5=Place("payannur","Kannur",564738,"abc")
# print(f"Name:{p1.name},district:{p1.district},pincode:{p1.pincode},landmark:{p1.landmark}")
# print(f"Name:{p2.name},district:{p2.district},pincode:{p2.pincode},landmark:{p2.landmark}")
# print(f"Name:{p3.name},district:{p3.district},pincode:{p3.pincode},landmark:{p3.landmark}")
# print(f"Name:{p4.name},district:{p4.district},pincode:{p4.pincode},landmark:{p4.landmark}")
# print(f"Name:{p5.name},district:{p5.district},pincode:{p5.pincode},landmark:{p5.landmark}")



# class Place:
#     def __init__(self,name,district,pincode):
#         self.name=name
#         self.district=district
#         self.pincode=pincode

#     def __str__(self):
#         return f"{self.name},{self.district},({self.pincode})"
    
    

# p1=Place("edakkad","kannur",670663)

# print(p1)


# class Myclass:
#     def __init__(self,subject1,subject2,subject3):
#         self.subject1=subject1
#         self.subject2=subject2
#         self.subject3=subject3

#     def __str__(self):
#         return f"subject:{self.subject1},subject2: {self.subject2},subject3: ({self.subject3})"
    
# s1=Myclass("dbms","oops","java")
# print(s1)
       


# class Myclass:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def Myfunction(self):
#         print(f"my name is  {self.age}")
# s1=Myclass("manoj",51)
# s1.age=40

# print(s1.Myfunction())        


class Info:
    def __init__(self,name,age,number):
        self.name=name
        self.age=age
        self.number=number
    
    def Myfunction(self):
        print(f"name: {self.name},age:{self.age},number: {self.number}")

p1=Info("sarang",32,9746988139)
p1.name="amal"
p1.age=25
p1.number=3456789023
p1.Myfunction()