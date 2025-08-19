

from abc import ABC, abstractmethod

class ATM(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

class SBI_ATM(ATM):
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited: {amount}. New Balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}. New Balance: {self.__balance}")
        else:
            print("Insufficient funds.")

# Usage
atm = SBI_ATM(5000)
atm.deposit(2000)       # Deposited: 2000. New Balance: 7000
atm.withdraw(1000)      # Withdrew: 1000. New Balance: 6000
