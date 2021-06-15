# Task 1
try:
    a = int(input('Введите трехзначное число: '))
    if 100 <= a <= 999:
        print(f'Сумма цифр введенного числа равна {a % 10 + (a % 100) // 10 + a // 100}')
    else:
        print('Число должно быть трехзначным')

except ValueError:
    print('Требуется ввести число')


# Task 2
x = 5
y = 6
print(f'{x} AND {y} = {x & y}')
print(f'{x} XOR {y} = {x^ y}')
print(f'{x} OR {y} = {x | y}')
print(f'{x}>>2 = {x >> 2}')
print(f'{x}<<2 = {x << 2}')

# Task 3

x, y = list(map(float, input('Введите координаты первой точки через запятую: ').split(',')))
x1, y1 = list(map(float, input('Введите координаты второй точки через запятую: ').split(',')))
k = (y1 - y) / (x1 - x)
b = (y - k * x)
print(f'y = {round(k, 3)}*x + {round(b, 3)}')

# Task 4

import random

x, y = list(map(int, input('Введите границы диапазона для вывода случайного целого числа через пробел: ').split()))

if x < y:
    print(random.randint(x, y))
else:
    print(random.randint(y, x))


x1, y1 = list(map(float,input('Введите границы диапазона для случайного вещественного числа через пробел: ').split()))

if x1 < y1:
    print(random.uniform(x1, y1))
else:
    print(random.uniform(y1, x1))


a, b = list(input('Введите границы диапазона для вывода случайного символа через пробел: ').split())
x2 = ord(a)
y2 = ord(b)
if x2 < y2:
    print(chr(random.randint(x2, y2)))
else:
    print(chr(random.randint(y2, x2)))

# Task 5
a, b = list(input('Введите две буквы через пробел: ').split())
dist = abs(ord(a)-ord(b)) - 1
print(ord(a))
if 65 <= ord(a) <= 90 and 65 <= ord(b) <= 90:
    print(f'Буква {a} находится на {ord(a) - 64} месте в алфавите')
    print(f'Буква {b} находится на {ord(b) - 64} месте в алфавите')
    print(f'Между {a} и {b} находятся {dist} букв(ы)')
elif 97 <= ord(a) <= 122 and 97 <= ord(b) <= 122:
    print(f'Буква {a} находится на {ord(a) - 96} месте в алфавите')
    print(f'Буква {b} находится на {ord(b) - 96} месте в алфавите')
    print(f'Между {a} и {b} находятся {dist} букв(ы)')
elif 1040 <= ord(a) <= 1071 and 1040 <= ord(b) <= 1071:
    print(f'Буква {a} находится на {ord(a) - 1039} месте в алфавите')
    print(f'Буква {b} находится на {ord(b) - 1039} месте в алфавите')
    print(f'Между {a} и {b} находятся {dist} букв(ы)')
elif 1072 <= ord(a) <= 1103 and 1072 <= ord(b) <= 1103:
    print(f'Буква {a} находится на {ord(a) - 1071} месте в алфавите')
    print(f'Буква {b} находится на {ord(b) - 1071} месте в алфавите')
    print(f'Между {a} и {b} находятся {dist} букв(ы)')
else:
    print('Обе буквы должны быть из английского или русского алфавита и написаны в одном регистре')

# Task 6
num = int(input('Введите номер буквы в русском алфавите '))
letter = chr(num + 1039)
if 1 <= num <= 33:
    print(f'Hа {num} месте в алфавите находится буква {letter}')
else:
    print('Введите номер от 1 до 33')

# Task 7

a, b, c = list(map(float, input('Введите длины сторон треугольника через пробел: ').split()))
if a + b > c and a + c > b and c + b > a:
    print(f'Из отрезков длиной {a}, {b}, {c} возможно составить треугольник')
else:
    print(f'Из отрезков длиной {a}, {b}, {c} невозможно составить треугольник')

# Task 8

year = int(input('Введите год: '))
if year % 4 == 0:
    print(f'{year} год является високосным')
else:
    print(f'{year} год не является високосным')

# Task 9
a, b, c = list(map(float, input('Введите три числа через пробел: ').split()))

if b < a < c or c < a < b:
    print(f'среднее = {a}')
elif a < b < c or c < b < a:
    print(f'среднее = {b}')
elif a < c < b or b < c < a:
    print(f'среднее = {c}')
else:
    print('Необходимо ввести три разных числа')


