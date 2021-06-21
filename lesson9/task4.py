class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool

    def go(self):
        print('Driving car')

    def stop(self):
        print('The car stopped')

    def turn(self, direction):
        print(f'The car turned {direction}')

    def show_speed(self):
        print(f'Speed = {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = False

    def show_speed(self):
        if self.speed > 60:
            print('Over speed')
        else:
            print(f'Speed = {self.speed}')


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = False


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = False

    def show_speed(self):
        if self.speed > 40:
            print('Over speed')
        else:
            print(f'Speed = {self.speed}')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


car1 = TownCar(100, 'black', 'mitsubishi')
print(car1.name, car1.color)
car1.go()
car1.stop()
car1.turn('right')
car1.show_speed()
print(car1.is_police)
print()
car2 = TownCar(40, 'black', 'mitsubishi')
car2.go()
car2.stop()
car2.turn('right')
car2.show_speed()
print(car2.is_police)
print()
car3 = SportCar(250, 'black', 'mitsubishi')
print(car3.name, car3.color)
car3.go()
car3.stop()
car3.turn('right')
car3.show_speed()
print(car3.is_police)
print()
car4 = WorkCar(35, 'black', 'mitsubishi')
print(car4.name, car4.color)
car4.go()
car4.stop()
car4.turn('right')
car4.show_speed()
print(car4.is_police)
print()
car5 = WorkCar(50, 'black', 'mitsubishi')
car5.go()
car5.stop()
car5.turn('right')
car5.show_speed()
print(car4.is_police)
print()
car6 = PoliceCar(120, 'black', 'mitsubishi')
print(car6.name, car6.color)
car6.go()
car6.stop()
car6.turn('right')
car6.show_speed()
print(car6.is_police)
