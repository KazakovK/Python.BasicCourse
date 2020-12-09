user_number = int(input('Введите целое положительное число: '))

max_number = 0

while user_number > 0:
    d = user_number % 10
    user_number //= 10

    if max_number < d:
        max_number = d

print('Максимальная цыфра в вашем числе: ', max_number,
      '\nПриходите еще!')