class Warehouse:
    def __init__(self):
        self.length = 10000
        self.width = 15000
        self.height = 50


class Equipment:
    def __init__(self, price, length, width, height):
        self.price = price
        self.length = length
        self.width = width
        self.height = height


class Printer(Equipment):
    def __init__(self, price, length, width, height, print_speed):
        super().__init__(price, length, width, height)
        self.print_speed = print_speed


class Scanner(Equipment):
    def __init__(self, price, length, width, height, type_scan):
        super().__init__(price, length, width, height)
        self.type_scan = type_scan


class Xerox(Equipment):
    def __init__(self, price, length, width, height, performance):
        super().__init__(price, length, width, height)
        self.performance = performance
