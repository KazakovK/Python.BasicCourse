from sys import argv

script_name, production, rate, prize = argv

wage = round((float(production) * float(rate)) + float(prize), 3)

print(f'''Выработка сотрудника в часах составляет: {production} часов; 
      Часовая ставка: {rate}  рублей;
      Премия: {prize} рублей;
      Итого зарплата составляет: {wage} рублей''')
