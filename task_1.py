my_list = [12, 3, 7.1, 'Строка', ('кортеж', 6, 9), None]


for el_list in my_list:
    val_list = el_list
    el_list = type(el_list)
    print(f'{val_list} - {el_list}')