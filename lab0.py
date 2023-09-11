class CreditCard:
    def __init__(self, card_number, balance):
        self.__account_number = card_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


account = CreditCard("4329 4032 1292 2504", 1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())