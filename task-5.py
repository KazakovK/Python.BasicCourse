class Stationery:
    def __init__(self):
        self.title = 'Фломастером'

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки Ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки Карандашом')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки Маркером')

a = Stationery()
b = Pen()
c = Pencil()
d = Handle()

a.draw()
b.draw()
c.draw()
d.draw()
