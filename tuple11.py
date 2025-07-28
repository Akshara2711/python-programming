x=("apple","banana","orange")
y=list(x)
y[1]="kiwi"
x=tuple(y)
print(x)




x=("apple","orange","kiwi")
y=list(x)
y[1]=("mango")
x=tuple(y)
print(x)




color=("blue","black","white")
y=list(color)
y[1]=("green")
x=tuple(y)
print(x)