class Node:
    def __init__(self,value):
        self.value=value
        self.children=[]

    def add_child(self,child):
        self.children.append(child)
    
    def display(self,level=0):
        print(" " * level*2+str(self.value))
        for child in self.children:
            child.display( level + 1)


root=Node("Root")

child1=Node("child1")
child2=Node("child2")
child3=Node("child3")

root.add_child(child1)
root.add_child(child2)
root.add_child(child3)

child1.add_child(Node("child 1.1"))
child2.add_child(Node("child 1.2"))
child3.add_child(Node("child 2.1"))

root.display()

