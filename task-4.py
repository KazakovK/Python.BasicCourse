user_word = input('Введите вашу фразу: ').split(' ')


for ind, word in enumerate(user_word):
    word = word[:10:1]
    print(ind, word)
