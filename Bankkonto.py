from abc import ABC, abstractmethod

class BankAccount(ABC):
    banks = ["SWEDBANK", "NORDEA", "DANSKEBANK"]
    next_bank_id = 1 
    
    def __init__(self, initial_balance):
        self.__bank_id = BankAccount.next_bank_id
        BankAccount.next_bank_id += 1
        self._balance = initial_balance

    @abstractmethod
    def check_out_banks(self, amount):
        pass

    @abstractmethod
    def return_banks(self, amount):
        pass

    def get_balance(self):
        return self._balance
        
    def set_balance(self, new_balance):
        self._balance = new_balance
    
    def get_bank_id(self):
        return self.__bank_id
    
    def delete_account(self):
        print("The bank account has been removed")
        del self
    
    @classmethod
    def bank_exists(cls, bank_name):
        return bank_name.upper() in cls.banks


class SavingsAccount(BankAccount):
    def __init__(self, initial_balance):
        super().__init__(initial_balance)

    def check_out_banks(self, amount):
        if amount > self._balance:
            print("Insufficient balance.")
        else:
            self._balance -= amount
            print(f"Checked out {amount}. New balance is {self._balance}")

    def return_banks(self, amount):
        self._balance += amount
        print(f"Returned {amount}. New balance is {self._balance}")

    def delete_account(self):
        super().delete_account()
        print("The savings account has been deleted")


class ATM:
    def __init__(self):
        self.accounts = []

    def create_account(self):
        initial_balance = float(input("Enter the initial balance: "))
        account = SavingsAccount(initial_balance)
        self.accounts.append(account)
        print(f"Account created with ID {account.get_bank_id()} and balance {account.get_balance()}")

    def find_account(self):
        account_id = int(input("Enter your account ID: "))
        for account in self.accounts:
            if account.get_bank_id() == account_id:
                return account
        print("Account not found.")
        return None

    def deposit(self):
        account = self.find_account()
        if account:
            amount = float(input("Enter amount to deposit: "))
            account.return_banks(amount)

    def withdraw(self):
        account = self.find_account()
        if account:
            amount = float(input("Enter amount to withdraw: "))
            account.check_out_banks(amount)

    def check_balance(self):
        account = self.find_account()
        if account:
            print(f"Your balance is: {account.get_balance()}")

    def delete_account(self):
        account = self.find_account()
        if account:
            self.accounts.remove(account)
            account.delete_account()
            print("Account has been deleted.")

    def run(self):
        while True:
            print("\nATM Menu:")
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Check Balance")
            print("5. Delete Account")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_account()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                self.check_balance()
            elif choice == '5':
                self.delete_account()
            elif choice == '6':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

# Example usage
if __name__ == "__main__":
    atm = ATM()
    atm.run()
