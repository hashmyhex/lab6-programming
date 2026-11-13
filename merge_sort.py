def merge_sort(items):
    if len(items) <= 1:
        return items

    middle = len(items) // 2
    left = merge_sort(items[:middle])
    right = merge_sort(items[middle:])

    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


numbers = [64, 25, 12, 22, 11, 90, 3, 25]
print(f"до сортировки: {numbers}")
print(f"после сортировки: {merge_sort(numbers)}")
print(f"совпадает со sorted == {merge_sort(numbers) == sorted(numbers)}")
