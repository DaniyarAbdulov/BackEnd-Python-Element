# Task 1 Гиппотенуза
import math
from math import sqrt
def hipotesa():
    try:
        a = int(input("Введите значение катета 1: "))
        b = int(input("Введите значение катета 2: "))
        c = sqrt(a**2 + b**2)
        print(f'Ответ: {c}')
    except ValueError:
        print(f'Введите число, а не букву')
        hipotesa()
hipotesa()

#Task 2 Число десятков

def desatki():
    try:
        number = int(input("Введите НЕотрицитальное число "))
        result = 0
        if number>0:
            result = ((number//10) % 10)
            print('Ответ: ',result)
        else:
            print("Попробуем еще раз: ")
            desatki()
    except ValueError:
        print("Введите число: ")
        desatki()
desatki()

#Task 3 Следующее четное

def chetnoe():
    try:
        n = int(input("Введите натуральное число: "))
        result = n+2-(n % 2)
        print("Следующее четное число: ", result)
    except ValueError:
        print("Введите целое число!")
        chetnoe()
chetnoe()


#Task 4 Последний урок
def school():

    lesson = int(input("Введите номер урока: "))
    five_min = lesson//2                     #малые перемены
    fifteen_min = lesson - five_min - 1      #большие перемены
    timming = lesson*45 + five_min*5 +fifteen_min*15         #считаем общезатраченное время

    hours = 9 + (timming//60)               #подсчет часов
    minutes = timming%60                    #подсчет минут
    print(f'Время окончания уроков {hours} : {minutes}')
school()

#Task 5 Какое число больше?
def comparison():
    try:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        if a>b:
            print("1")
        elif b>a:
            print("2")
        else:
            print("0")
    except ValueError:
        print("Нужно вводить числа")
        comparison()
comparison()

#Task 6 Максимум из трех
def maximum():
    try:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        c = int(input("Введите третье число: "))
        print(f'наибольшее значение: {max(a,b,c)}')
    except ValueError:
        print("Вводите число, а не буквы ")
        maximum()
maximum()

#Task 7 Ладья
def lada():
    try:
        x1 = int(input("Введите координаты Ладьи по оси Х: "))
        y1 = int(input("Введите координаты Ладьи по оси Y: "))
        x2 = int(input("Введите координаты другой фигуры по оси Х: "))
        y2 = int(input("Введите координаты другой фигуры по оси Y: "))
        if x1 == x2 or y1 == y2:
            print(f'YES')
        else:
            print(f'NO')
    except:
        print(f'Введите координаты (числа), а не буквы!')
        lada()

lada()

#Task 8 Существует ли треугольник?

def triangle():
    try:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        c = int(input("Введите третье число: "))
        if a+b>c and b+c>a and a+c>b:
            print(f'YES')
        else:
            print(f'NO')
    except ValueError:
        print(f'Вводите числа, а не буквы')
        triangle()
triangle()


#Task 9 Количество равных из трех

def equality():
    try:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        c = int(input("Введите третье число: "))
        if a==b==c:
            print(f'число совпадений: 3')
        elif a==b or b==c or a==c:
            print(f'число совпадений: 2')
        else:
            print(f'число совпадений: 0')


    except ValueError:
        print(f'Вводите числа, а не буквы')
        equality()
equality()

#Task 10 Упорядочить три числа
def last_of_us():
    try:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        c = int(input("Введите третье число: "))
        if a > b:
            a, b = b, a
        if b > c:
            b, c = c, b
        if a > b:
            a, b = b, a
        print(a, b, c)

    except ValueError:
        print(f'Вводите числа, а не буквы')
        last_of_us()
last_of_us()
