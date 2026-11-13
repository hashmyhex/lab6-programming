def show(name, matrix):
    print(f"{name}:")
    for row in matrix:
        print(row)


def add(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return None
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def sub(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return None
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def mul(a, b):
    # столбцов в a должно быть столько же, сколько строк в b
    if len(a[0]) != len(b):
        return None
    result = [[0] * len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result


a = [[1, 2, 3], [4, 5, 6]]
b = [[7, 8, 9], [1, 2, 3]]
c = [[1, 2], [3, 4], [5, 6]]

show("a", a)
show("b", b)
show("c", c)
show("a + b", add(a, b))
show("a - b", sub(a, b))
show("a * c", mul(a, c))

if add(a, c) is None:
    print("a + c: размеры не совпадают")
if mul(a, b) is None:
    print("a * b: нельзя перемножить")
