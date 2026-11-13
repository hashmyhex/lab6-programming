list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print(f"list1: {list1}")
print(f"list2: {list2}")

set1 = set(list1)
set2 = set(list2)

print(f"объединение: {sorted(set1 | set2)}")
print(f"пересечение: {sorted(set1 & set2)}")
print(f"разность: {sorted(set1 - set2)}")

# то же самое, но с сохранением порядка
union_ordered = list1 + [x for x in list2 if x not in list1]
intersection_ordered = [x for x in list1 if x in list2]
difference_ordered = [x for x in list1 if x not in list2]
print(f"объединение по порядку: {union_ordered}")
print(f"пересечение по порядку: {intersection_ordered}")
print(f"разность по порядку: {difference_ordered}")
