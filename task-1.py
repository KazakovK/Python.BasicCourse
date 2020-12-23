try:
    with open('task_1.txt', 'w', encoding='UTF-8') as file_object:
        el = 0
        user_list = []
        while el != ' \n':
            el = input('Введите строку для записи (для оконания записи введите пробел) : ') + '\n'
            user_list.append(el)
            print(user_list)
        file_object.writelines(user_list)

except IOError:
    print('Произошла ошибка, данные не записаны!')
