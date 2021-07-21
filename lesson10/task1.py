class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        for line in self.matrix:
            for i in line:
                print(i, end=' ')
            print()
        return f''

    def __add__(self, other_matrix):
        matrix_sum = [[num1 + num2 for num1, num2 in zip(line1, line2)] for line1, line2, in
                      zip(self.matrix, other_matrix.matrix)]
        return '\n'.join([' '.join(map(str, line)) for line in matrix_sum])


a = [
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
]

b = [
    [4, 3, 2],
    [4, 3, 2],
    [4, 3, 2]
]

matrix1 = Matrix(a)
matrix2 = Matrix(b)

print(matrix1)
print(matrix2)

print(matrix1 + matrix2)
