class Student:
    def __init__(self,name,rollno,s1mark,s2mark,s3mark,s4mark,s5mark):
        self.name=name
        self.rollno=rollno
        self.s1mark=s1mark
        self.s2mark=s2mark
        self.s3mark=s3mark
        self.s4mark=s4mark
        self.s5mark=s5mark
    def Myfunction(self):
        print("name"+self.rollno)

    def __str__(self):
        return(f"name: {self.name},rollno: {self.rollno},s1mark: {self.s1mark},s2mark: {self.s2mark},s3mark: {self.s3mark},s4mark: {self.s4mark},s5mark: {self.s5mark}")
p1=Student("anu",5,60,28,89,57,78)
print(p1)  

class Student:
    def __init__(self,name,rollno,s1mark,s2mark,s3mark,s4mark,s5mark):
        self.name=name
        self.rollno=rollno
        self.s1mark=s1mark
        self.s2mark=s2mark
        self.s3mark=s3mark
        self.s4mark=s4mark
        self.s5mark=s5mark

    def Myfunction(self):
        print("name"+self.rollno)

    def __str__(self):
        return(f"name: {self.name},rollno: {self.rollno},s1mark: {self.s1mark},s2mark: {self.s2mark},s3mark:{self.s3mark},s4mark: {self.s4mark},s5mark: {self.s5mark}")
p1=Student("achu",4,89,88,98,95,100)
print(p1)          


class Bankaccount:
         def __init__(self,account_holder,balance):
              self.account_holders=account_holder
              self.balance=balance

         
    
         def __str__(self):
              return(f"account_holders: {self.account_holders},balance: {self.balance}")
    
         def get_balance(self):
           return self.balance

class Customer(Bankaccount):
    def __init__(self, account_holder, balance):
        super().__init__(account_holder, balance)
  
    

    def deposits(self):
        return(f"depositedamount: {self.deposits()},balance: {self.balance}")
    

    
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient funds!")
        else :
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

p1=Customer("ammu",200000)
print(p1)
p1.withdraw(20000)


p1.deposits=500000
print(p1.deposits)
p1.withdraw=300000

      



class LibraryBook:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow_book(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f'You have borrowed "{self.title}" by {self.author}.')
        else:
            print(f'Sorry, "{self.title}" is already borrowed.')

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f'You have returned "{self.title}".')
        else:
            print(f'"{self.title}" was not borrowed.')

    def display_status(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        print(f'"{self.title}" by {self.author} is currently: {status}')