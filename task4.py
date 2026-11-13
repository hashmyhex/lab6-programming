students = [
    ("Иван", 25, 4.5),
    ("Мария", 22, 4.8),
    ("Пётр", 30, 4.2),
    ("Анна", 20, 4.9),
    ("Олег", 23, 3.9),
]

oldest = max(students, key=lambda s: s[1])
print(f"самый старший: {oldest[0]}, {oldest[1]} лет")

best = max(students, key=lambda s: s[2])
print(f"лучший студент: {best[0]}, балл {best[2]}")

avg_age = sum(s[1] for s in students) / len(students)
print(f"средний возраст == {avg_age:.1f}")

print("по баллу (по убыванию):")
for name, age, gpa in sorted(students, key=lambda s: s[2], reverse=True):
    print(f"{name}: {gpa}")
