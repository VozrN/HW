def get_matrix(n, m, value):
    matrix = []
    if int(n) * int(m) * int(value) <= 0:
        return matrix
    else:
        for i in range(int(n)):
            m_1 = []
            matrix.append(m_1)
            for j in range(int(m)):
                matrix[i].append(value)
        return matrix


n = input('Введите количество строк: ')
m = input('Введите количество столбцов: ')
value = input('Введите значение: ')
print(get_matrix(n, m, value))
