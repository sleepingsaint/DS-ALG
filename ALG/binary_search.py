# normal search function
# assuming only distinct elements are in list
def search(lst, value):
    if value in lst:
        return lst.index(value)
    return -1


# binary Search function
# assuming list is sorted and distinct
def binary_search(lst, value):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (high + low) // 2
        if lst[mid] == value:
            return mid
        elif lst[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# test cases
test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val2))
