try:
    with open('task-3.txt', 'r', encoding='UTF-8') as file_object:
        count_person = 0
        sum_person = 0
        person = []
        for line in file_object:
            count_person += 1
            list_person = line.split('-')
            sum_person = sum_person + int(list_person[1])
            avg_sum = sum_person / count_person
            if int(list_person[1]) >= 20000:
                person.append(list_person[0])
        print('Сотрудники с доходом более 20 т.р.: ', person)
        print(f'Средний доход сотрудников составляет: {avg_sum}')

except IOError:
    print('Ошибка!')
