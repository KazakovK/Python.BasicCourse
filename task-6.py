from itertools import count, cycle

list_count = []
for el in count(3):
    if el > 10:
        break
    else:
        list_count.append(el)
print(list_count)

check = 1
for el in cycle('повторение'):
    if check > 13:
        break
    else:
        print(el)
        check += 1
