def system():
    print('Введите число которое нужно перевести')
    x = int(input())
    print('В какую систему счисления перевести. Введите число')
    n = int(input())
    a = []
    from math import floor
    while x >= n:
        c = x - floor(x / n) * n
        if c == 10:
            c = 'A'
        elif c == 11:
            c = 'B'
        elif c == 12:
            c = 'C'
        elif c == 13:
            c = 'D'
        elif c == 14:
            c = 'E'
        elif c == 15:
            c = 'F'
        a.append(c)
        x = floor(x / n)
    if x == 10:
        x = 'A'
    elif x == 11:
        x = 'B'
    elif x == 12:
        x = 'C'
    elif x == 13:
        x = 'D'
    elif x == 14:
        x = 'E'
    elif x == 15:
        x = 'F'
    print(x, *a[::-1], sep='')
    print('Нужно перевести еще число? Если да, то нажмите "д", если нет, то нажмите "н"')
    cod = input()
    while cod != 'д' and cod != 'н':
        print('Введите корректный символ')
        cod = input()
    if cod == 'д':
        system()
    elif cod == 'н':
        print('Спасибо за использование программы')
system()
