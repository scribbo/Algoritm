from random import random

def task_1():
    num = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    for i in range(2, 100):
        for j in range(2, 10):
            if i % j == 0:
                num[j] += 1
    print(f'количество чисел от 2 до 99, кратных числам от 2 до 9 равно : {num}')

#task_1()


def task_2():


    N = 10
    a = [0] * N
    b = []
    for i in range(N):
        a[i] = int(random() * 15)
        if a[i] % 2 == 0:
            b.append(i + 1)
    print(f'В массиве {a} четные числа имеют индексы: {b}')

#task_2()


def task_3():

    N = 15
    a = [0] * N
    b = []
    min_index = 0
    max_index = 0
    for i in range(N):
        a[i] = int(random() * 99)

        if a[i] < a[min_index]:
            min_index = i
        if a[i] > a[max_index]:
            max_index = i
    print(a)
    a[min_index], a[max_index] = a[max_index], a[min_index]
    print(a)

#task_3()


def task_4():

    N = 50
    a = [0] * N
    b = {}

    for i in range(N):
        a[i] = int(random() * 10)
        if b.get(a[i]) == None:
            b[a[i]] = 1
        else:
            b.update({a[i]: b[a[i]] + 1})

    max_value = 0
    for el in b.items():
        if el[1] > max_value:
            max_keys = []
            max_keys.append(el[0])
            max_value = el[1]
        elif el[1] == max_value:
            max_keys.append(el[0])
    print(a)
    print(f'В массиве выше чаще всего встречаются: {max_keys} ({max_value} раз)')


#task_4()
# [4, 4, 5, 6, 4, 0, 1, 1, 2, 0, 6, 6, 9, 6, 2, 2, 9, 4, 4, 9, 9, 7, 2, 7, 5, 8, 8, 0, 3, 0, 7, 4, 3, 2, 5, 0, 8, 2, 2, 6, 6, 9, 4, 1, 9, 6, 7, 1, 7, 9]
# В массиве выше чаще всего встречаются: [4, 6, 2, 9] (7 раз)


def task_8():

    M = 4
    N = 4
    A = []
    for i in range(N):
        row = input(f'Введите {M} элемента строки матрицы: ').split()
        sum_row = 0
        for i in range(len(row)):
            row[i] = int(row[i])
            sum_row += row[i]
        row.append(sum_row)
        A.append(row)
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(A[i][j], end=' ')
        print()
task_8()








