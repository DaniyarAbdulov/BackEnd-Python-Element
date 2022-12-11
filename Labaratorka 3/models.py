import hashlib
from enum import Enum
from typing import Optional
from typing import List


class Wallet_Type(Enum):
    KZT = 'KZT'
    USD = 'USD'
    RUB = 'RUB'





class BankAccount:
    balance = 0


    def __init__(self, name: str, surname: str, account: Wallet_Type):
        self.name = name
        self.surname = surname
        self.account = Wallet_Type


    # def  addToBankAccount(self, summa: int):
    #     self.balance += summa
    #     return self.balance
    #
    # def substractFromBankAccount(self, summa: int):
    #     if self.balance<summa:
    #         print('Недостаточно средств!')
    #     self.balance-=summa
    #     return self.balance



    def __repr__(self):
        return f'{self.name}, {self.surname}, {self.account.KZT}'


# danik = BankAccount(name='Danik', surname='Danik', account = Wallet_Type.KZT, balance=100)
# print(danik)
