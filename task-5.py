revenue = float(input('Укажите прибыль компании за год, тыс.руб.: '))
lesion = float(input('Укажите убуток компании за год, тыс.руб: '))

if revenue > lesion:
    result = 'Прибыльно'
elif revenue == lesion:
    result = 'Нейтрально'
else:
    result = 'Убыточно'

profit = revenue - lesion
profitability = profit / revenue * 100

if result == 'Прибыльно':
    print('Ваша фирма работает: ', result, '\nРентабильность выручки составлет:',
          '{:.2f}'.format(profitability), '%')
else:
    print('Ваша фирма работает: ', result)

employees = int(input('Укажите количество сотруников в компании: '))
profit_employees = profit / employees

print('Прибыль на одного сотружника составляет:', '{:.2f}'.format(profit_employees), ', тыс.руб.')