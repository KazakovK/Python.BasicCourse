try:
    with open('task_4.txt', 'r', encoding='UTF-8') as file_object:
        list_new = []
        for line in file_object:
            list_user = line.split(' — ')
            list_user[1] = list_user[1].rstrip()
            if list_user[0] == 'One':
                list_user[0] = 'Один'
            elif list_user[0] == 'Two':
                list_user[0] = 'Два'
            elif list_user[0] == 'Three':
                list_user[0] = 'Три'
            else:
                list_user[0] = 'Четыре'
            with open('task_4_2.txt', 'a', encoding='UTF-8') as file_object2:
                print(f'{list_user[0]} - {list_user[1]}', file=file_object2)
except IOError:
    print('Ошибка!')
