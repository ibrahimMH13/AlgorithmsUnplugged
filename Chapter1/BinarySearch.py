a = range(5, 5000)


# binary_search rely on sort list according values
# so need ordered list
def binary_search(a, value, left, right):
    while left <= right:
        middle = (left + right) // 2
        if a[middle] == value:
            return middle
        if a[middle] > value:
            right = middle - 1
        if a[middle] < value:
            left = middle + 1
    return "NOT FOUND"


value = 1
key = binary_search(a, value, 0, len(a))
print(f"this value [{value}] hold in index no[{key}] in this range ")
