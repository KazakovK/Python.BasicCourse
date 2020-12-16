el = []
while el != 'exit':
    el_new = input('Введите числа через пробел (Если ввод завершен введите "exit"): ').split(' ')
    if el_new.count('exit') > 0:
        el_new.remove('exit')
        el.extend(el_new)
        break
    el.extend(el_new)
    print('Сумма элементов:', sum(map(int, el)))

print('Программа завершила работу. Итог:', sum(map(int, el)))
