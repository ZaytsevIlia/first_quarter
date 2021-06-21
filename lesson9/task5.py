class Stationery:
    def __init__(self, title=str):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title=str):
        super().__init__(title=str)
        self.title = 'Pen'

    def draw(self):
        print('Ручка рисует')


class Pencil(Stationery):
    def __init__(self, title=str):
        super().__init__(title=str)
        self.title = 'Pencil'

    def draw(self):
        print('Карандаш рисует')


class Handle(Stationery):
    def __init__(self, title=str):
        super().__init__(title=str)
        self.title = 'Handle'

    def draw(self):
        print('Маркер рисует')


object1 = Pen()
object1.draw()
object2 = Pencil()
object2.draw()
object3 = Handle()
object3.draw()


