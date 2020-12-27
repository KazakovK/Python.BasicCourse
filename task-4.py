class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        self.direction = direction
        print(f'Машина повернула на {direction}')

    def show_speed(self):
        print(f'Скорость автомобиля: {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police, length):
        super().__init__(speed, color, name, is_police)
        self.length = length

    def show_speed(self):
        if self.speed > 60:
            print(f'Вы первысили скорость!!!')
        else:
            print('Скорость в норме :)')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police, overclocking):
        super().__init__(speed, color, name, is_police)
        self.overclocking = overclocking


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police, consumption):
        super().__init__(speed, color, name, is_police)
        self.consumption = consumption

    def show_speed(self):
        if self.speed > 40:
            print(f'Вы первысили скорость!!!')
        else:
            print('Скорость в норме :)')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police, reliability):
        super().__init__(speed, color, name, is_police)
        self.reliability = reliability


car = Car(70, 'Зеленая', 'Лада', 0)

townCar = TownCar(80, 'Красная', 'Шкода', 0, 180)
sportCar = SportCar(180, 'Синяя', 'Феррари', 0, 6.7)
workCar = WorkCar(30, 'Серая', 'Рено', 0, 8.7)
policeCar = PoliceCar(90, 'Сине-белая', 'Лада', 1, 'Надежная')

print(f'Обчная: Скорость: {car.speed}, цвет: {car.color}, марка: {car.name}, полицейская: {car.is_police}')
print(f'Городская: Скорость: {townCar.speed}, цвет: {townCar.color}, марка: {townCar.name},'
      f'полицейская: {townCar.is_police}, длина: {townCar.length}')
print(f'Спортивная: Скорость: {sportCar.speed}, цвет: {sportCar.color}, марка: {sportCar.name},'
      f'полицейская: {sportCar.is_police}, разгон: {sportCar.overclocking}')
print(f'Рабочая: Скорость: {workCar.speed}, цвет: {workCar.color}, марка: {workCar.name},'
      f'полицейская: {workCar.is_police}, расход топлива: {workCar.consumption}')
print(f'Полицейская: Скорость: {policeCar.speed}, цвет: {policeCar.color}, марка: {policeCar.name},'
      f'полицейская: {policeCar.is_police}, надежность: {policeCar.reliability}')

car.go()
car.stop()
car.turn('Лево')
car.show_speed()

townCar.show_speed()
workCar.show_speed()