goods = []
number = 1
while number < 100000:
    goods_new = input('Ведите новый новар через запятую в формате (название, цена, кол., ед.измерения).'
                      'Если ввод товаров завершен введите "нет" :').split(',')
    if goods_new[0] == 'нет':
        break
    else:
        goods_list = {'название': goods_new[0], 'цена': goods_new[1], 'количество': goods_new[2],
                      'ед': goods_new[3]}
        goods_list_number = (number, goods_list)
        goods.append(goods_list_number)
        number = number + 1

name = []
price = []
counter = []
measurement = []

for el in goods:
    goods_dict = el[1]
    name.append(goods_dict.get('название'))
    price.append(goods_dict.get('цена'))
    counter.append(goods_dict.get('количество'))
    measurement.append(goods_dict.get('ед'))

summary_dict = {'название': name, 'цена': price, 'количество': counter, 'ед': measurement, }
print(summary_dict)
