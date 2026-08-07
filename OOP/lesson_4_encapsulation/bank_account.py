

class BankAccount:
    
    def __init__(self, account_holder, initial_balance):
        self.__account_holder = account_holder
        self.__balance = initial_balance
        self.__transaction_count = 0
        
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__transaction_count += 1
            print(f"Deposited ${amount}. New balance is: ${self.__balance}")
            return True
        print("Deposit amount must be positive!")
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__transaction_count += 1
            print(f"Withdrew ${amount}. New balance is: ${self.__balance}")
            return True
        print("Invalid withdrawal amount!")
        return False
    
    def get_balance(self):
        return self.__balance
    
    def get_account_holder(self):
        return self.__account_holder
    
    def get_transaction_count(self):
        return self.__transaction_count
    
    def account_info(self):
        print(f"Account Holder: {self.__account_holder}")
        print(f"Balance: ${self.__balance}")
        print(f"Transactions: {self.__transaction_count}")
        
# Test all
account = BankAccount("Gurudev", 10000000)
account.deposit(5000000)
account.withdraw(2500000)
account.withdraw(50000000)
account.account_info

