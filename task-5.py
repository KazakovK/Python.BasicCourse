rating = [8, 7, 5, 3, 3, 2]

rating_val = int(input('Введите новый элемент рейтинга: '))
position_rating = 0
try:

    if rating_val == 9:
        rating.insert(0, rating_val)
    elif rating_val == 1:
        rating.insert(len(rating), rating_val)
    else:
        position_rating = rating.index(rating_val)
        rating.insert(position_rating, rating_val)

except ValueError:
    for el in rating:
        if el > rating_val:
            position_rating = rating.index(el) + 1
    rating.insert(position_rating, rating_val)
print(rating)
