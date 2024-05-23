from abc import ABC, abstractmethod

# Abstrakt basklass för bankkonto
class BankAccount(ABC):
    banks = ["SWEDBANK", "NORDEA", "DANSKEBANK"]  # Lista över tillgängliga banker
    next_bank_id = 1  # Statisk variabel för att hålla reda på nästa unika bank-ID
    
    def __init__(self, initial_balance):
        self.__bank_id = BankAccount.next_bank_id  # Tilldela unikt bank-ID
        BankAccount.next_bank_id += 1  # Inkrementera nästa bank-ID
        self._balance = initial_balance  # Sätt initialt saldo

    # Abstrakt metod för uttag
    @abstractmethod
    def check_out_banks(self, amount):
        pass

    # Abstrakt metod för insättning
    @abstractmethod
    def return_banks(self, amount):
        pass

    # Metod för att hämta saldo
    def get_balance(self):
        return self._balance
        
    # Metod för att sätta ett nytt saldo
    def set_balance(self, new_balance):
        self._balance = new_balance
    
    # Metod för att hämta bank-ID
    def get_bank_id(self):
        return self.__bank_id
    
    # Metod för att radera konto
    def delete_account(self):
        print("The bank account has been removed")
        del self
    
    # Klassmetod för att kontrollera om en bank finns i listan
    @classmethod
    def bank_exists(cls, bank_name):
        return bank_name.upper() in cls.banks


# Sparkonto som ärver från BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, initial_balance):
        super().__init__(initial_balance)  # Anropa basklassens konstruktor

    # Implementera uttag
    def check_out_banks(self, amount):
        if amount > self._balance:
            print("Insufficient balance.")  # Kontrollera om tillräckligt saldo finns
        else:
            self._balance -= amount  # Minska saldo
            print(f"Checked out {amount}. New balance is {self._balance}")

    # Implementera insättning
    def return_banks(self, amount):
        self._balance += amount  # Öka saldo
        print(f"Returned {amount}. New balance is {self._balance}")

    # Överskugga delete_account för att radera sparkontot
    def delete_account(self):
        super().delete_account()
        print("The savings account has been deleted")


# ATM-klass för att hantera konton och interaktion
class ATM:
    def __init__(self):
        self.accounts = []  # Lista över konton

    # Skapa nytt konto
    def create_account(self):
        initial_balance = float(input("Enter the initial balance: "))
        account = SavingsAccount(initial_balance)  # Skapa ett nytt sparkonto
        self.accounts.append(account)  # Lägg till kontot i listan
        print(f"Account created with ID {account.get_bank_id()} and balance {account.get_balance()}")

    # Hitta ett konto baserat på ID
    def find_account(self):
        account_id = int(input("Enter your account ID: "))
        for account in self.accounts:
            if account.get_bank_id() == account_id:
                return account  # Returnera hittat konto
        print("Account not found.")
        return None

    # Hantera insättning
    def deposit(self):
        account = self.find_account()
        if account:
            amount = float(input("Enter amount to deposit: "))
            account.return_banks(amount)

    # Hantera uttag
    def withdraw(self):
        account = self.find_account()
        if account:
            amount = float(input("Enter amount to withdraw: "))
            account.check_out_banks(amount)

    # Kontrollera saldo
    def check_balance(self):
        account = self.find_account()
        if account:
            print(f"Your balance is: {account.get_balance()}")

    # Radera konto
    def delete_account(self):
        account = self.find_account()
        if account:
            self.accounts.remove(account)  # Ta bort konto från listan
            account.delete_account()
            print("Account has been deleted.")

    # Kör huvudmenyn och hanterar användarens val
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

# Starta ATM-applikationen
if __name__ == "__main__":
    atm = ATM()
    atm.run()
