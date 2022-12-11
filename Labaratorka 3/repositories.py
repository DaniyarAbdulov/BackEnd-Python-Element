from typing import List, Optional

from models import BankAccount, Wallet_Type


class BankAccount_Repositories:
    bank_account_users: List[BankAccount] = []

    def create_bank_account_user(self, name: str, surname: str, account: Wallet_Type) -> None:
        user = BankAccount(name=name, surname=surname, account=account)
        self.bank_account_users.append(user)

    def get_bank_account_user(self, name: str, surname: str) -> Optional[BankAccount]:
        user = next((u for u in self.bank_account_users if name == u.name and surname == u.surname), None)

        if not user:
            print('Bank account not found')
            return
        return user

    def addToBankAccount(self, balance: int, summa: int):
        self.addToBankAccount(balance=balance, summa=summa)

    def substractFromBankAccount(self, balance: int, summa: int):
        self.substractFromBankAccount(balance=balance, summa=summa)
