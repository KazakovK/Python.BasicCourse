class NotIntError(Exception):
    def __init__(self, error_text):
        self.error_text = error_text


user_list = []
user_el = None

while user_el != "stop":
    try:
        user_el = input('Введите число: ')
        user_el = float(user_el)
        user_list.append(user_el)
    except ValueError:
        try:
            raise NotIntError("Вы ввели не число!")
        except NotIntError as err:
            print(err)

print(user_list)
