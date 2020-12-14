user_list = input('Введите значения для списка через запятую: ').split(',')

el_next = 0

for el in range(0, len(user_list), 2):
    el = el
    el_next = el + 1
    if el_next >= len(user_list):
        break
    user_list[el], user_list[el_next] = user_list[el_next], user_list[el]

print(user_list)
