class Person:
  def __init__(self, name, number):
    self.name = name
    self.number = number

  def printname(self):
    print(self.name, self.number)

class Doctor(Person):
  def __init__(self,name,number):

    super().__init__(name, number)

x = Doctor("Ammu", "8765543338")
x.printname()
