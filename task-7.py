try:
    with open('task_7.txt', 'r', encoding='UTF-8') as file_object:
        avg_profit = 0
        count_profit = 0
        dict_firm = {}
        for line in file_object:
            list_firm = line.split(' ')
            profit = int(list_firm[2]) - int(list_firm[3])
            list_firm.append(profit)
            if list_firm[4] > 0:
                avg_profit = avg_profit + list_firm[4]
                count_profit += 1
            dict_new = {list_firm[0]: profit}
            dict_firm.update(dict_new)

except IOError:
    print('Ошибка файл не прочитан!')

avg_profit = avg_profit / count_profit
dict_profit = {'average_profit': avg_profit}
list_itog = [dict_firm, dict_profit]
print(list_itog)

import json

with open("task_7.json", "w+") as new_file:
    json.dump(list_itog, new_file)
