from time import sleep


class TrafficLight:
    __color = str

    def running(self):
        while True:
            self.__color = 'Красный'
            print(self.__color)
            sleep(7)
            self.__color = 'Жёлтый'
            print(self.__color)
            sleep(2)
            self.__color = 'Зелёный'
            print(self.__color)
            sleep(5)


my_obj = TrafficLight()
my_obj.running()
