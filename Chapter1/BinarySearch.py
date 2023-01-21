a = range(5, 5000)


def binary_search(a, value, left, right):
    while left <= right:
        middle = (left + right) // 2
        print(middle)
        if a[middle] == value:
            return middle
        if a[middle] > value:
            right = middle -1
        if a[middle] < value:
            left = middle +1
    return "NOT FOUND"

print(binary_search(a, 52, 0,len(a)))