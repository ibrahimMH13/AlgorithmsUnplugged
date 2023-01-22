


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


def binary_search_recursive(a,value,right,left):
    if left > right:
        return "NOT FOUND"
    middle = (left + right) // 2
    if a[middle] == value:
        return middle
    if a[middle] > value:
        binary_search_recursive(a,value,left,middle-1)
    if a[middle]< value:
        binary_search_recursive(a,value,left+1,right)
    return "NOT FOUND"


a = range(5, 5000)
value = 10
key = binary_search(a, value, 0, len(a))
key_recursive = binary_search(a, value, 0, len(a))
print(f"this value [{value}] hold in index no[{key}] in this range ")
print(f"recursive this value [{value}] hold in index no[{key}] in this range ")
