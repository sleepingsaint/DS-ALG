def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if high > low:
        i = low
        pivot = arr[high]
        k = high
        while i < k and i < high:
            while arr[i] > pivot:
                arr[i], arr[k], arr[k-1] = arr[k-1], arr[i], arr[k]
                k -= 1
            i += 1
        quick_sort(arr,  0, k-1)
        quick_sort(arr, k+1, high)


# test cases
arr1 = [10, 7, 8, 9, 1, 5]
quick_sort(arr1)
print(arr1)