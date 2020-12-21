from functools import reduce

generator = (par for par in range(100, 1001, 2))


def func_sum(prev_el, el):
    return prev_el + el


print(reduce(func_sum, generator))
