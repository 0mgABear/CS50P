# version 1

balance = 0

def main():
  print("Balance:", balance)

if __name__ == "__main__":
  main()

# v 1.1 - does not work, unboundlocalerror

balance = 0

def main():
  print("Balance:", balance)
  deposit(100)
  withdraw(50)
  print("Balance:", balance)

def deposit(n):
  balance += n

def withdraw(n):
  balance -= n

if __name__ == "__main__":
  main()

# v 1.2
balance = 0

def main():
  print("Balance:", balance)
  deposit(100)
  withdraw(50)
  print("Balance:", balance)

def deposit(n):
  global balance
  balance += n

def withdraw(n):
  global balance
  balance -= n

if __name__ == "__main__":
  main()

# version 2 - using OOP
class Account:
  def __init__(self):
    self._balance = 0 #private

  def balance(self):
    return self._balance
  
  def deposit(self, n):
    self._balance += n
  
  def wihdraw(self, n):
    self._balance -= n

def main():
  account = Account()
  print("Balance: ", account.balance)
  account.deposit(100)
  account.wihdraw(50)
  print("Balance: ", account.balance)