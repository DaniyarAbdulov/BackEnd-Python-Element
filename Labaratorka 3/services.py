from models import BankAccount, Wallet_Type
from repositories import BankAccount_Repositories
from typing import Optional

class BankServices:
    repositories: BankAccount_Repositories

    def __init__(self, repositories: BankAccount_Repositories):
        self.repositories = repositories

    def create_bank_account_user(self, name: str, surname:str, account: Wallet_Type) -> None:
        self.repositories.create_bank_account_user(name = name, surname=surname, account=account)
        self._send_email_verification(email=surname)

    def get_bank_account_user(self, name: str, surname: str) -> Optional[BankAccount]:
        return self.repositories.get_bank_account_user(name = name, surname=surname)

    def addToBankAccount(self, balance: int, summa:int) ->None:
        self.addToBankAccount(balance=balance, summa=summa)

    def substractFromBankAccount(self, balance: int, summa: int)-> None:
        self.substractFromBankAccount(balance=balance, summa=summa)






    @staticmethod
    def _send_email_verification(email: str) -> None:
        print(f'send verification letter to {email}')







