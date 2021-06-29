def task_1():
    company = {}
    n = int(input('Количество предприятий: '))
    s = 0
    for i in range(n):
        name = input(str(i+1) + '-е предприятие: ')
        profit_1, profit_2, profit_3, profit_4 = list(map(float, input('Прибыль по кварталам: ').split()))
        year_profit = profit_1 + profit_2 + profit_3 + profit_4
        company[name] = year_profit
        s += year_profit

    av_comp = s / n
    losers = []
    print('Предприятия с прибылью выше среднего: ')
    for i in company:
        if company[i] >= av_comp:
            print(i)
        else:
            losers.append(i)

    print('Предприятия с прибылью ниже среднего: ')
    for el in losers:
        print(el)

# task_1()


def task_2():
    from collections import deque

    signs = '0123456789ABCDEF'
    hex2dec = {}
    dec2hex = {}
    n = 0
    for el in signs:
        hex2dec[el] = n
        dec2hex[n] = el
        n += 1
    # print(hex2dec)
    # print(dec2hex)

    def num_dec(string):
        dec = 0
        num = deque(string)
        for i in range(len(num)):
            dec += hex2dec[num.pop()] * 16 ** i
        return dec

    def num_hex(res):
        n_hex = deque()
        while res > 0:
            s = res % 16
            n_hex.appendleft(dec2hex[s])
            res //= 16
        return list(n_hex)

    num_1 = num_dec(input('Введите первое число в шестнадцатиричной системе исчисления: ').upper())
    num_2 = num_dec(input('Введите второе число в шестнадцатиричной системе исчисления: ').upper())

    print(f'Сумма чисел равна {num_hex(num_1 + num_2)}')
    print(f'Произведение чисел равно {num_hex(num_1 * num_2)}')


task_2()

