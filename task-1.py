class Matrix:
    def __init__(self, arr: list):
        self.arr = arr

    def __str__(self):
        v = f'Матричный вид:'
        for el in self.arr:
            v = v + f'\n{el}'
        return v

    def __add__(self, other):
        counter = 0
        sum_matrix = []
        for el in self.arr:
            sum_array = [el[i] + other.arr[counter][i] for i in range(len(el))]
            counter += 1
            sum_matrix.append(sum_array)
        sum_matrix = Matrix(sum_matrix)
        return sum_matrix


matrix_1 = Matrix([[1, 3, 6], [36, 8, 11]])
matrix_2 = Matrix([[1, 7, 6], [12, 3, 12]])

print(matrix_1)
print(matrix_2)

matrix_3 = matrix_1 + matrix_2

print(matrix_3)
