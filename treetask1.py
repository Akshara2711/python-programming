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


root=Node("food")

a=Node("fruits")
b=Node("vegitables")
c=Node("grains")

root.add_child(a)           
root.add_child(b)                             
root.add_child(c)

a1=Node("citrus")
a2=Node("Berries")
a11=Node("orange")
a12=Node("lemon")
a21=Node("strawberry")
a22=Node("Blueberry")

b1=Node("leafy")
b2=Node("Root")
b11=Node("spinach")
b12=Node("Lettuce")
b21=Node("carrot")
b22=Node("Beetroot")

c1=Node("Rice")
c2=Node("wheat")

a.add_child(a1)
a.add_child(a2)                             
a1.add_child(a11)
a1.add_child(a12)
a2.add_child(a21)
a2.add_child(a22)

b.add_child(b1)
b.add_child(b2)
b1.add_child(b11)
b1.add_child(b12)
b2.add_child(b21)
b2.add_child(b22)

c.add_child(c1)
c.add_child(c2)

root.display()