class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
     
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₱{amount}. New balance: ₱{self.balance}")
        else:
            print("Deposit amount must be greater than zero.")
    
    def withdraw(self, amount):
        
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₱{amount}. New balance: ₱{self.balance}")
        else:
            print("Insufficient funds for this withdrawal.")
    
    def display_balance(self):
        
        print(f"Account balance: ₱{self.balance}")


account = BankAccount("123456789", "Bobby Porta", 500)


account.deposit(200)       
account.withdraw(100)      
account.withdraw(700)      
account.display_balance()   
