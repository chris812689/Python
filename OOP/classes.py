class User:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        


# user1 = User("Chris")
# user2 = User("Gavin")

class Comment:
    def __init__(self, username, text, likes =0):
        self.username = username
        self.text = text
        self.likes = likes

# c = Comment("davey123", "lol you're so silly", 3)
# print(c.username)

class BankAccount:
     
    def __init__(self, name):
        self.owner = name
        self.balance = 0.0
    
    def __reper__(self):
        return f"{self.owner}"
 
    def getBalance(self):
        return self.balance
 
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
 
    def deposit(self, amount):
        self.balance += amount
        return self.balance



acct = BankAccount("Darcy")
acct.owner #Darcy
acct.balance #0.0
acct.deposit(10)  #10.0
# acct.withdraw(3)  #7.0
# acct.balance(3)  #7.0