user_number = input('Введите целое положительное число: ')

n = int(user_number)
nn = int(user_number + user_number)
nnn = int(user_number + user_number + user_number)

sum_user_number = n + nn + nnn
print('Сумма чисел n+nn+nnn, где n=', user_number, "составит: ", sum_user_number,
      '\nСпасибо что использете наш сервис!')
