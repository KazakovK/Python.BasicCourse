class Coat:
    def __init__(self, coat_v):
        self.consumption = coat_v / 6.5 + 0.5


class Costume:
    def __init__(self, H):
        self.consumption = 2 * H + 0.3


class Clothing:
    def __init__(self, name):
        self.name = name
        self.coat_count = []
        self.costume_count = []

    def add_coat(self, V):
        self.coat_count.append(Coat(V).consumption)

    def add_costume(self, H):
        self.costume_count.append(Costume(H).consumption)

    def total_expense(self):
        total_expense = sum(self.coat_count) + sum(self.costume_count)
        return total_expense

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


r = Clothing('Одежда')
r.add_coat(46)
r.add_coat(42)
r.add_costume(2.2)
r.add_costume(1.86)

r.name = "Итого на пошив одежды будет затрачено: "
print(f'{r.name} {round(r.total_expense(), 2)} \n')
