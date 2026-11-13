from collections import Counter

numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3, 7]
print(f"список: {numbers}")

# через подсчёт
counts = Counter(numbers)
duplicates = [num for num, count in counts.items() if count > 1]
print(f"дубликаты через Counter: {duplicates}")
for num in duplicates:
    print(f"{num}: встречается {counts[num]} раз(а)")

# через множества
seen = set()
duplicates2 = set()
for num in numbers:
    if num in seen:
        duplicates2.add(num)
    seen.add(num)
print(f"дубликаты через set: {sorted(duplicates2)}")

if not duplicates:
    print("дубликатов нет")
