try:
    with open('task_6.txt', 'r', encoding='UTF-8') as file_object:
        dict_tem = []
        for line in file_object:
            list_tem = line.split(' ')
            dict_tem.append(list_tem)

except IOError:
    print('Ошибка открытия файла!')

dict_itog = {}
for i in range(0, len(dict_tem), 1):
    dict_tem[i][2] = dict_tem[i][2].replace('—', '0')
    dict_tem[i][2] = dict_tem[i][2].replace('(пр)', '')
    dict_tem[i][2] = int(dict_tem[i][2])
    dict_new = {dict_tem[i][0]: dict_tem[i][2]}
    dict_itog.update(dict_new)
print(dict_itog)
