class ZeroError(Exception):
    def __init__(self, error_text):
        self.error_text = error_text


user_input = input("Введите делимое и делитель через запятую: ").split(",")

dividend, divider = int(user_input[0]), int(user_input[1])

try:
    if divider == 0:
        raise ZeroError("Делитель не может быть равным 0!!!")
    inp_data = dividend / divider
except ZeroError as err:
    print(err)
else:
    print(f"Результат деления: {inp_data}")
