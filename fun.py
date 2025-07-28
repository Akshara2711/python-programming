def Myfunction(fname):
    print(fname + "manoj")
Myfunction("akshara")
Myfunction("abhijith")  


def Myfunction(*kids):
    print("the youngest child is" + kids[2])

Myfunction("ammu","ponnu","achu")  


def Myfunction(child1,child2,child3):
    print("the youngest child is"+child3 )

Myfunction(child1="ammu",child2="anju",child3="achu")  


def Myfunction(**kids):
    print("he is the first child" + "lname")

Myfunction(fname="tobbie",lname="ammu")