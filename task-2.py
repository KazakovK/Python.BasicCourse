time = int(input('Здравствуйте.Введите период времени в секундах: '))
hour = time // 3600
minute = (time - hour * 3600) // 60
second = (time - hour * 3600 - minute * 60)
print('Ваше время составит: ', '%02d:%02d:%02d' % (hour, minute, second), '\nСпасибо что выбрали наш конвертер!')