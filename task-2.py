class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self._weight_sm = 25
        self._thickness = 5


    def asphalt_mass(self):
        mass = (self._length * self._width * self._weight_sm * self._thickness)/1000
        print(f'При ширине {self._length} м. и длине {self._width} м., масса асфальта составит: {mass} т.\n'
              f'С учетом расчетной массы на сантиметр {self._weight_sm} и покрытии в {self._thickness} см.')

a = int(input('Укажите ширину дороги в метрах: '))
b = int(input('Укажите длину дороги в метрах: '))
start = Road(a,b)
start.asphalt_mass()