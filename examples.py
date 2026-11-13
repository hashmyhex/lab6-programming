# списки
fruits = ["яблоко", "банан", "вишня"]
fruits.append("груша")
fruits.insert(1, "апельсин")
fruits.remove("банан")
last = fruits.pop()
print(f"fruits == {fruits}, pop вернул {last}")
print(f"индекс вишни == {fruits.index('вишня')}")

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort(reverse=True)
print(f"по убыванию: {numbers}")
squares = [x**2 for x in range(1, 6)]
print(f"квадраты: {squares}")

# срезы
data = [10, 20, 30, 40, 50, 60, 70, 80]
print(f"data[2:5] == {data[2:5]}")
print(f"data[::2] == {data[::2]}")
print(f"data[::-1] == {data[::-1]}")
print(f"data[-3:] == {data[-3:]}")
half = len(data) // 2
print(f"половины: {data[:half]} и {data[half:]}")

# кортежи
point = (3, 4)
x, y = point
print(f"point == {point}, x == {x}, y == {y}")
try:
    point[0] = 10
except TypeError as error:
    print(f"кортеж менять нельзя: {error}")
