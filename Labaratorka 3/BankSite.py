
import sys
from models import BankAccount, Wallet_Type
from repositories import BankAccount_Repositories
from typing import Optional
from services import BankServices
from handlers import Bank_User_Handlers


# def addToBankAccount(balance:int, summa: int):
#     balance += summa
#     return balance
#
#
# def substractFromBankAccount(balance:int, summa: int):
#     if balance < summa:
#         print('Недостаточно средств!')
#     balance -= summa
#     return balance


def init():

    global surname, name
    bank_repositories = BankAccount_Repositories ()
    bank_services = BankServices (repositories=bank_repositories)
    bank_handlers = Bank_User_Handlers (services=bank_services)


    while True:
        current_wallet = 0
        choice = int(input('Добро пожаловать в наш Банк.\nПройдете регистрацию?\n 1 = Да, 2 = Нет '))
        if choice == 1:
            name, surname = input('Введите имя и фамилию ').split(' ')
            account = Wallet_Type.KZT

            bank_handlers.registration(name=name, surname=surname, account=account)

            print(bank_repositories.create_bank_account_user(name, surname, account))
            print('Вы прошли регистрацию!')
        if choice == 2:
            print("Досвидания! ")
            break
        choice2 = int(input('Хотите войти в банк-аккаунт?\n1 да 2 нет '))
        if choice2 == 1:
            name, surname = input('Введите имя и фамилию ').split(' ')
            print(bank_handlers.sign_in(name=name, surname=surname))

        choice3 = int(input('Хотите внести сумму на ваш счет? 1 - Да, 2 - Нет '))
        if choice3 == 1:
            summa = int(input('Укажите сумму, которую вы хотите внести: '))
            bank_services.addToBankAccount(balance=current_wallet, summa=summa)
            print(f'Сумма {summa} была внесена на ваш счет. Ваш баланс равен {current_wallet} ')




        elif choice2 == 2:
            print("Досвидания! ")
            break

if __name__ == '__main__':
    init()





