from models import BankAccount, Wallet_Type
from repositories import BankAccount_Repositories
from typing import Optional

from services import BankServices


class Bank_User_Handlers:
    services: BankServices

    def __init__(self, services: BankServices):

        self.services = services


    def registration(self, name: str, surname: str, account: Wallet_Type):
        name = name.strip()
        surname = name.strip()
        account = Wallet_Type.RUB.USD.KZT

        self.services.create_bank_account_user(name=name, surname=surname, account=account)

    def sign_in(self, name: str, surname:str) -> Optional[BankAccount]:
        name = name.strip()
        surname= surname.strip()
        return self.services.get_bank_account_user(name = name, surname=surname)

    def addToBankAccount(self, balance: int, summa: int):
        summa = int(summa)
        balance = balance
        return self.services.addToBankAccount(balance=balance, summa=summa)

    def substractFromBankAccount(self, balance: int, summa: int):
        summa = int(summa)
        balance = balance
        return self.services.addToBankAccount(balance=balance, summa=summa)



