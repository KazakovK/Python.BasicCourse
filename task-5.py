equipment = {}


class Warehouse:
    def __init__(self):
        self.length = 10000
        self.width = 15000
        self.height = 50


class Equipment:
    def __init__(self, id_eq, price, name, quantity, subdivision):
        self.id_eq = id_eq
        self.price = price
        self.name = name
        self.quantity = quantity
        self.subdivision = subdivision

    def add_equipment(self):
        other = [self.name, self.price, self.quantity, self.subdivision]
        other_update = {self.id_eq: other}
        equipment.update(other_update)


class Printer(Equipment):
    def __init__(self, id_eq, price, name, quantity, subdivision, print_speed):
        super().__init__(id_eq, price, name, quantity, subdivision)
        self.print_speed = print_speed

    def add_equipment(self):
        other = [self.name, self.price, self.quantity, self.subdivision, self.print_speed]
        other_update = {self.id_eq: other}
        equipment.update(other_update)


class Scanner(Equipment):
    def __init__(self, id_eq, price, name, quantity, subdivision, type_scan):
        super().__init__(id_eq, price, name, quantity, subdivision)
        self.type_scan = type_scan

    def add_equipment(self):
        other = [self.name, self.price, self.quantity, self.subdivision, self.type_scan]
        other_update = {self.id_eq: other}
        equipment.update(other_update)


class Xerox(Equipment):
    def __init__(self, id_eq, price, name, quantity, subdivision, performance):
        super().__init__(id_eq, price, name, quantity, subdivision)
        self.performance = performance

    def add_equipment(self):
        other = [self.name, self.price, self.quantity, self.subdivision, self.performance]
        other_update = {self.id_eq: other}
        equipment.update(other_update)


a = Equipment(1, 12.10, "HP", 1, "Маркетинг")
a.add_equipment()
b = Equipment(2, 13.10, "LG", 1, "Фин.отдел")
b.add_equipment()
print(equipment)
