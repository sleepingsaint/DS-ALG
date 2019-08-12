# defining the bubble sort function
def bubble_sort(lst):
    for j in range(len(lst)):
        for i in range(len(lst) - j - 1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
            i += 1
    return lst

# test case
sort_list = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(sort_list))

