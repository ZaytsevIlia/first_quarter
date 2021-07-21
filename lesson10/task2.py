from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, parameter):
        self.parameter = parameter

    @abstractmethod
    def calculation(self):
        pass


class Coat(Clothes):
    @property
    def calculation(self):
        return round((self.parameter / 6.5 + 0.5), 2)


class Suit(Clothes):
    @property
    def calculation(self):
        return round((2 * self.parameter + 0.3), 2)


my_clothes1 = Coat(10)
my_clothes2 = Suit(15)

print(my_clothes1.calculation)
print(my_clothes2.calculation)
