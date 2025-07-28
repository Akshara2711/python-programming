def calculator(y,operatore):
    x=2
    if operatore=="Addition assignment":
         x+=y
         return x
  
    elif operatore=="substract assignment":
        x-=y
        return x
    elif operatore=="multiplication assignment":
        x*=y
        return x
    elif operatore=="division assignment":
        x/=y
        return x
    elif operatore=="modules assignment":
        x%=y
        return x
    elif operatore=="Exponentiation assignment":
      x**=y
      return x
    elif operatore=="floor divisin assignment":
        x//=y
        return x
    else:
        return "invalid operator"
    




print("Assignment:", calculator( 0, "assignment"))
print("Addition assignment:", calculator( 3, "add assignment"))
print("substraction assignment:", calculator( 3, "substract assignment"))
print("multiplication assignment:", calculator( 3, "multiplication assignment"))
print("division assignment:", calculator(3, "division assignment"))
print("modules assignment:", calculator( 3, "modules assignment"))
print("Exponentiation assignment:", calculator( 3, "Exponentiation assignment"))
print("floor divisin assignment:", calculator( 3, "floor divisin assignment"))
