def int_func(word):
    return word.title()


user_word = input('Введите слово или словосочетание:')
print(f'Ваше предложение первосходно!\n"{int_func(user_word)}"')
