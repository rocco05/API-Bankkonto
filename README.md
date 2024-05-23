Bankkonto ATM-simulator

Introduktion
Den här Python-applikationen simulerar en enkel ATM-maskin där användare kan skapa bankkonton, sätta in pengar, ta ut pengar, kontrollera sitt saldo och radera sina konton. Applikationen använder objektorienterad programmering och implementerar abstrakta klasser för att hantera olika typer av bankkonton.

Funktioner
Skapa konto: Användare kan skapa nya bankkonton med ett startbelopp.
Insättning: Användare kan sätta in pengar på sina konton.
Uttag: Användare kan ta ut pengar från sina konton.
Kontrollera saldo: Användare kan kontrollera sitt kontosaldo.
Radera konto: Användare kan radera sina konton.

Krav
Python 3.12.x

Installation
Klona eller ladda ner detta repository till din lokala maskin.
Navigera till katalogen där filerna finns.

Användning
Kör följande kommando i din terminal eller kommandotolk för att starta applikationen:

Huvudmeny
När du kör programmet kommer huvudmenyn att visas. Följ instruktionerna på skärmen för att navigera genom de olika funktionerna i ATM-simulatorn.


ATM Menu:
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Delete Account
6. Exit
Enter your choice:

Klassbeskrivningar
BankAccount (Abstrakt klass)
banks: En lista över tillgängliga banker.
next_bank_id: En statisk variabel som håller koll på nästa unika bank-ID.
balance: En statisk variabel för att simulera kontobalans.
__init__(self, initial_balance): Initierar ett nytt bankkonto med ett startbelopp.
check_out_banks(self, amount): Abstrakt metod för uttag.
return_banks(self, amount): Abstrakt metod för insättning.
get_balance(self): Returnerar kontots saldo.
set_balance(self, new_balance): Sätter ett nytt saldo.
get_bank_id(self): Returnerar kontots unika ID.
delete_account(self): Raderar kontot.
bank_exists(cls, bank_name): Kontrollerar om en bank finns i listan över banker.
SavingsAccount (ärver BankAccount)
__init__(self, initial_balance): Initierar ett nytt sparkonto med ett startbelopp.
check_out_banks(self, amount): Hanterar uttag från kontot.
return_banks(self, amount): Hanterar insättning på kontot.
delete_account(self): Raderar sparkontot.
ATM
__init__(self): Initierar en lista över konton.
create_account(self): Skapar ett nytt konto.
find_account(self): Hittar ett konto baserat på användarens konto-ID.
deposit(self): Hanterar insättning på ett konto.
withdraw(self): Hanterar uttag från ett konto.
check_balance(self): Visar saldot på ett konto.
delete_account(self): Raderar ett konto.
run(self): Kör huvudmenyn och hanterar användarens val.

Exempel
När programmet körs kan användaren skapa ett konto, sätta in pengar, ta ut pengar, kontrollera saldo och radera sitt konto. Nedan följer ett exempel på hur användaren kan interagera med programmet:
1. Användaren startar programmet och väljer att skapa ett nytt konto och bestämmer hur mycket man vill ha på sitt konto.
2. Användaren väljer att sätta in pengar på kontot.
3. Användaren tar ut så mycket pengar som man vill.
4. Användaren kontrollerar sitt saldo.
5. Användaren väljer att radera sitt konto.
6. Användaren avslutar sin ATM.







