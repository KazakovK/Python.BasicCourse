class Cell:
    def __init__(self, count_units):
        self.count_units = count_units

    def __add__(self, other):
        return Cell(self.count_units + other.count_units)

    def __sub__(self, other):
        if self.count_units > other.count_units:
            return Cell(self.count_units - other.count_units)
        else:
            new_cell = Cell('невозможно!')
            return new_cell

    def __mul__(self, other):
        return Cell(self.count_units * other.count_units)

    def __floordiv__(self, other):
        return Cell(self.count_units // other.count_units)

    def make_order(self, count_row):
        counter = self.count_units // count_row
        new_row = ''
        while counter > 0:
            new_row += '*****\n'
            counter -= 1
        if self.count_units % count_row > 0:
            counter = self.count_units % count_row
            while counter > 0:
                new_row += '*'
                counter -= 1
        return new_row


cell_1 = Cell(10)
cell_2 = Cell(13)

cell_3 = cell_1 + cell_2
cell_4 = cell_1 - cell_2
cell_5 = cell_1 * cell_2
cell_6 = cell_1 // cell_2
print(f'Сложение клеток: {cell_3.count_units}')
print(f'Вычитание клеток: {cell_4.count_units}')
print(f'Умножение клеток: {cell_5.count_units}')
print(f'Деление клеток: {cell_6.count_units}')

print(f'Разложение ячеек клетки о рядам: \n{cell_1.make_order(4)}')
