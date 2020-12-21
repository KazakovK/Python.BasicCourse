# Вариант 1
n = int(input('Введите значение факториал которого необходимо получить: '))


def fact(n):
    for el in range(1, n + 1):
        yield el


factor = 1
for el in fact(n):
    factor = factor * el

print(f'Факториал числа составляет: {factor}')

# Вариант 2
from math import factorial


def fact(n):
    for el in range(1, n + 1):
        el = factorial(el)
        yield el


for elt in fact(n):
    print(elt)
