matrix = [
    [1, 2, 3],
    [4, 5, 6],
]

# через zip
transposed = [list(row) for row in zip(*matrix)]

# то же самое циклами, чтобы проверить
rows = len(matrix)
cols = len(matrix[0])
check = [[0] * rows for _ in range(cols)]
for i in range(rows):
    for j in range(cols):
        check[j][i] = matrix[i][j]

print("исходная матрица:")
for row in matrix:
    print(row)

print("транспонированная матрица:")
for row in transposed:
    print(row)

print(f"циклами получилось то же самое == {check == transposed}")
