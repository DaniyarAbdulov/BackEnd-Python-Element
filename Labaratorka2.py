# 1.Четные числа
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
while a<=b:
    if a%2 == 0:
        print(a)
    a+=1

# 2. Милимальный делитель
a = int(input('Введите натуральное число: '))
i = 2
while a % i != 0:
    i+=1
print(i)

# 3. Делители числа
a = int(input('Введите натуральное число: '))
number = 1
while number<= a:
    if a%number == 0:
        print(number, end=' ')
    number+=1

# 4. Сумма чисел
num1 = int(input('Введите натуральное число: '))
c = 0
for i in range(num1):
    num2 = int(input('Введите натуральное число: '))
    c+=num2
print(f'={c}')

# 5. Перевод числа
import math
a = input('Введите число: ')
res = 0
degree = 0
for i in reversed(range(0, len(a))):
    res+= (int(a[i]))*int(math.pow(2,degree))
    degree+=1
print(res)



# 6. Степень
import math
def duoble_power():
    a = float(input('Введите вещественное число: '))
    n = int(input('Введите целое неотрецательное число: '))
    c = pow(a, n)
    print(f'{c:.0f}')
duoble_power()

# 7. Голосование
def election(x,y,z):
    sum = x + y +z
    if (sum>=2):
        return 1
    else:
        return 0

a = input().split()
print(election(int(a[0]), int(a[1]), int(a[2])))

# 8. Банк
def Add_to(bank_account, a):
    bank_account +=a
    return bank_account
def Minus_from(bank_account, a):
    bank_account-=a
    return bank_account

def Exchange(money, currency_from, currency_to):
    match currency_from, currency_to:
        case 'USD', 'KZT':
            return money*470
        case 'KZT', 'USD':
            return money/470
        case 'EUR', 'KZT':
            return money*480
        case 'KZT', 'EUR':
            return money/480

money = 10000
print(Add_to(money, 200))
print(Minus_from(money, 200))
print(Exchange(money, 'USD', 'KZT'))
print(Exchange(money, 'KZT', 'USD'))
print(Exchange(money, 'EUR', 'KZT'))
print(Exchange(money, 'KZT', 'EUR'))


