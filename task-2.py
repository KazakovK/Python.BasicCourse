def func_person(name, surname, year, city, mail, phone):
    print(f'Имя сотрудника: {name}, Фамилия: {surname}, Год рождения: {year}, '
                 f'Город: {city}, Почта: {mail}, Телефон: {phone}')


a, b, c, d, e, f = input('Введите через запятую: Имя,Фамилию, Год рождения,Город,E-mail,Телефон: ').split(',')

func_person(surname=b, year=c, name=a, city=d, mail=e, phone=f)
