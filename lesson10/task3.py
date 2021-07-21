class BiologicalCell:
    def __init__(self, cell):
        self.cell = cell

    def __str__(self):
        return f'В клетке {self.cell} ячеек'

    def __add__(self, other):
        self.cell = self.cell + other.cell
        return self.cell

    def __sub__(self, other):
        if self.cell > other.cell:
            self.cell = self.cell - other.cell
            return self.cell
        else:
            return 'В первой клетке ячеек меньше чем во второй.'

    def __mul__(self, other):
        self.cell = self.cell * other.cell
        return self.cell

    def __truediv__(self, other):
        self.cell = self.cell // other.cell
        return self.cell

    def make_order(self, row):
        return '\n'.join(['*' * row for _ in range(self.cell // row)]) + '\n' + '*' * (self.cell % row)


a = BiologicalCell(15)
b = BiologicalCell(10)

print(a)
print(b)
print(a * b)
print(a + b)
print(a - b)
print(a / b)
print(a)
print(a.make_order(4))





    # (__add__()), вычитание(__sub__()), умножение(__mul__()), деление(__floordiv____truediv__()).