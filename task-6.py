current_result = float(input('Укажите текщий результат  километрах: '))
planned_result = float(input('Укажите планируемый результ: '))

days_result = float(current_result)
days = 1

while days_result <= planned_result:
    days_result = days_result * 1.1
    days = days + 1

print('На', days, 'день спортсмен достигнет результата - не менее', planned_result, 'км (',
      '{:.2f}'.format(days_result), ' км).\nСпасибо что используете наш сервис!')
