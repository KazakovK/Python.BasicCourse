def my_func_in(x: int, y: int):
    return round(x ** y, 4)


def my_func_out(x: int, y: int):
    z = x
    for el in range(1, abs(y), 1):
        z = z * x
    return round(1 / z, 4)


a, b = input('Введите целые положительное и отрицательное число через запятую: ').split(',')

print('Встроенная функция:', my_func_in(int(a), int(b)))
print('Функция через цикл:', my_func_out(int(a), int(b)))
