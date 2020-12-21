default_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_list = [default_list[el] for el in range(1, len(default_list)) if default_list[el] > default_list[el - 1]]

print(new_list)
