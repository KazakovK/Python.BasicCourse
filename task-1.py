class Dater:
    def __init__(self, date):
        self.date = date

    @staticmethod
    def number_validation(date):
        spliter = date.split("-")
        day, mon, yars = int(spliter[0]), int(spliter[1]), int(spliter[2])
        if day < 0 or day > 31:
            print('Некорретно указан день!')
        if mon < 0 or mon > 12:
            print('Некорретно указан месяц!')
        if yars < 0 or yars > 3000:
            print('Некорретно указан год!')

    @classmethod
    def number_format(cls, date):
        spliter = date.split("-")
        day, mon, yars = int(spliter[0]), int(spliter[1]), int(spliter[2])
        print(f'День {day} Месяц {mon} Год {yars}')


a = input('Введите дату в формате «день-месяц-год»: ')
Dater.number_format(a)
Dater.number_validation(a)
