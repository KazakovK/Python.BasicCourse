try:
    with open('task_5.txt', 'w+', encoding='UTF-8') as file_object:
        for el in range(1, 100, 2):
            file_object.write(str(el))
            file_object.write(' ')
        file_object.seek(0)
        list_sum = file_object.read().split(' ')
        list_sum = [int(el) for el in list_sum if el != '']
        itog_sum = 0
        for i in list_sum:
            itog_sum = itog_sum + i
        print(f'Итоговая сумма: {itog_sum}')
except IOError:
    print('Ошибка создания файла!')
