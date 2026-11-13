import random

n = int(input("введите N: "))

if n < 1:
    print("N должно быть больше 0")
else:
    numbers = [random.randint(1, 20) for _ in range(n)]
    print(f"исходный список: {numbers}")

    print(f"сумма == {sum(numbers)}")
    print(f"среднее == {sum(numbers) / n:.2f}")
    print(f"минимум == {min(numbers)}")
    print(f"максимум == {max(numbers)}")

    print(f"отсортированный: {sorted(numbers)}")

    # dict запоминает порядок добавления, поэтому порядок не теряется
    unique = list(dict.fromkeys(numbers))
    print(f"без дубликатов: {unique}")
