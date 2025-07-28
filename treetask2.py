class Node:
    def __init__(self,value):
        self.value=value
        self.childern=[]
    def add_child(self,child):
        self.childern.append(child)

    def display(self,level=0):
        print(" " * level * 2+str(self.value))
        for child in self.childern:
            child.display( level + 1)

root=Node("Vehicles")

a=Node("Land")
b=Node("water")
c=Node("air")


root.add_child(a)           
root.add_child(b)                             
root.add_child(c)

a1=Node("cars")
a2=Node("Motorcycles")
a11=Node("Sedan")
a12=Node("SUV")
a21=Node("Cruiser")
a22=Node("Sport")

b1=Node("Boat")
b2=Node("ship")

c1=Node("Airplane")
c2=Node("Helicopter")

a.add_child(a1)
a.add_child(a2)
a1.add_child(a11)
a1.add_child(a12)
a2.add_child(a21)
a2.add_child(a22)

b.add_child(b1)
b.add_child(b2)

c.add_child(c1)
c.add_child(c2)

root.display()