class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_masses(self):
        return f'{self._width * self._length * 25 * 5} т.'


my_obj = Road(12, 23)
print(my_obj.asphalt_masses())
