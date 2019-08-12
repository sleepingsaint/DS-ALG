# main merge sort function
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        a = merge_sort(arr[:mid])
        b = merge_sort(arr[mid:])
        return merge(a, b)
    elif len(arr) == 1:
        return arr

# helper function to merge two arrays
def merge(a, b):
    i = j = k = 0
    c = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        elif a[i] > b[j]:
            c.append(b[j])
            j += 1
        k += 1
    c.extend(a[i:])
    c.extend(b[j:])
    return c

# test cases
arr1 = [12, 11, 13, 5, 6, 7]
arr2 = [8, 7, 9]

print(merge_sort(arr2))
