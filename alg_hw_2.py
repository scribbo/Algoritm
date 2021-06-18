# Task 1

def operation(a, b):
    try:
        operator = input('Введите арифметический оператор или 0 для выхода: ')
    except ValueError:
        print('Введите +, -, * или /')
        operation(a, b)

    if operator == '+':
        print(f'Сумма чисел {a} и {b} равна {a + b}')
    elif operator == '-':
        print(f'Разность чисел {a} и {b} равна {a - b}')
    elif operator == '*':
        print(f'Произведение чисел {a} и {b} равно {a * b}')
    elif operator == '/':
        if b != 0:
            print(f'Частное от деления чисел {a} и {b} равно {a / b}')
        else:
            print('На ноль делить нельзя')
    elif operator == '0':
        global to_break
        to_break = True
    else:
        print('Оператор не распознан, попробуйте еще раз')
        operation(a, b)


while True:
    to_break = False
    try:
        a, b = list(map(float, input('Введите два числа ').split()))
        operation(a, b)
    except ValueError:
        print('Числа не распознаны')
        continue
    if to_break:
        break

Task 2

num = input('Введите число: ')
even = 0
odd = 0
for i in range(len(num)):
    if int(num[i]) % 2 == 0:
        even += 1
    else:
        odd += 1
print(f'В числе {num} {even} четных цифр и {odd} нечетных')

# Task 3

num = input('Введите число:')
num_rev = ''
for i in range(len(num)):
    num_rev += num[len(num) - i - 1]

print(num_rev)

# Task 4
n = int(input())


def my_sum(n):
    if n == 0:
        return 1
    else:
        return my_sum(n-1) + (-0.5) ** n


print(my_sum(n))

# Task 5

for i in range(32, 128):
    print(f'{i} {chr(i)}')

# Task 6

import random

a = random.randint(10, 100)
i = 0
while i < 10:
    n = int(input('Введите число: '))
    if n == a:
        print('Вы угадали!')
    elif n > a:
        print('Загаданное число меньше')
        i += 1
    else:
        print('Загаданное число больше')
        i += 1
print(f'Ваши попытки исчерпаны. Загаданное число: {a}')

# Task 7

import random


def my_sum(n):
    if n == 1:
        return 1
    else:
        return my_sum(n-1) + n


n = random.randint(1, 1000)
if my_sum(n) == (n * (n + 1) / 2):
    print('Равенство верно')
else:
    print('Равенство не верно')



# Task 8

qtty, num = list(map(int, input('Введите количество чисел и искомую цифру ').split()))

my_str = ''
for i in range(qtty):
    a = int(random.uniform(0, 1000))
    my_str += str(a)
    i += 1

k = 0
for el in my_str:
    if int(el) == num:
        k += 1
print(f'В введенной последовательности чисел {my_str} цифра {num} встречается {k} раз(а)')

# Task 9

num_list = list(input('Введите ряд натуральных чисел: ').split())

sum_list = []
for el in num_list:
    sum_el = 0
    for i in range(len(el)):
        sum_el += int(el[i])
    sum_list.append(sum_el)

max_sum = 0
for j in range(len(sum_list) - 1):
    if sum_list[j] > max_sum:
        max_sum = sum_list[j+1]
        max_index = j + 1
    else:
        max_sum = sum_list[j]
        max_index = j


print(f'Максимальная сумма цифр у числа {num_list[max_index]}, она равна {max_sum}')







