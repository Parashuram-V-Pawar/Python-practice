class BankAccount:
    def __init__(self, acc_number : int, balance : float):
        self.acc_number = acc_number
        self.__balance = balance

    def display_balance(self):
        return self.__balance
    
    def deposit(self, amount: float):
        self.__balance += amount
        print("Deposit successful.")
    
    def withdraw(self, amount: float):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"\nWithdrawl successful.")
        else:
            print("Insufficient balance!")

def operations(acc_number, balance):
    details = BankAccount(acc_number, balance)
    while True:
        print("What do you want to do:\n1. Check balance\n2. Deposit\n3. Withdraw\n4. Exit")
        n = int(input("Enter your choice in number(1, 2, 3, 4): "))
        match n:
            case 1: print(f"\nBalance is: {details.display_balance()}\n")
            case 2: 
                amount = float(input("Enter deposit amount: "))
                details.deposit(amount)
                print(f"Current balance is: {details.display_balance()}\n")
            case 3:
                amount = float(input("Enter withdrawl amount: "))
                details.withdraw(amount)
                print(f"Remaining balance is: {details.display_balance()}\n")
            case 4:
                break
            case _:
                print("Please enter valid choice.")
    print("Thank you visit again...")

def main():
    print("Welcome to Bank")
    operations(2917801, 234523.56)

if __name__=="__main__":
    main()         
