try:
    with open('task_2.txt', 'r', encoding='UTF-8') as file_object:
        count_line = 0
        for line in file_object:
            count_line += 1
            count_simv = len(line.split(' '))
            print(f'Количество слов в строке {count_line}: {count_simv}')
    print(f'Строк в файле: {count_line}')
except IOError:
    print('Произошла ошибка!')
