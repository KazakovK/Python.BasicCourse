def func_division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'На ноль делить нельзя'


dividend = float(input("Введите делимое: "))
divider = float(input("Введите делитель: "))
print('Результат деления:', round(func_division(dividend, divider), 2))
