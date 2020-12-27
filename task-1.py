import time


class TrafficLight:
    def __init__(self):
        self.__color = ('red', 'yellow', 'green')

    def running(self):
        el = 0
        stop = None
        while True:
            print(self.__color[el])
            if self.__color[el] == 'red':
                time.sleep(7)
            elif self.__color[el] == 'yellow':
                time.sleep(2)
            else:
                time.sleep(13)
            el += 1
            if el > 2:
                el = 0


TrafficLight = TrafficLight()
print(TrafficLight.running())
