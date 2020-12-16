def my_func(a, b, c):
    my_list = [a, b, c]
    max_first = max(my_list)
    my_list.remove(max_first)
    max_second = max(my_list)
    return max_first + max_second


number_one, number_two, number_three = input("Введите 3 числа через запятую: ").split(',')

print(my_func(float(number_one), float(number_two), float(number_three)))
