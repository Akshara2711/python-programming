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

child1=Node("fruits")                                     
child2=Node("vegitables")
child3=Node("grains")
child4=Node(" ")
child5=Node(" ")

root.add_child(child1)
root.add_child(child2)                             
root.add_child(child3)

x="citrus 1.1"
a="orange 1.2"
b="Lemon 1.3"

child1.add_child(Node(x))
child1.add_child(Node("orange 1.2"))
child1.add_child(Node("Lemon 1.3"))
child1.add_child(Node("Berries 1.4"))
child1.add_child(Node("strawberry"))
child1.add_child(Node("Blueberry"))

x.add_

child2.add_child(Node("Leafy 2.1"))
child2.add_child(Node("Spinach 2.2"))
child2.add_child(Node("Lettuce"))
child2.add_child(Node("Root"))
child2.add_child(Node("carrot"))
child2.add_child(Node("Beetroot"))

child3.add_child(Node("Rice 3.1"))
child3.add_child(Node("wheat 3.2"))

root.display()