def quicksort(array):
    if len(array) == 1:
        return array
    low = 0
    high = len(array) - 1
    pivot = array[high]
    while low < high:
        while array[low] > pivot:
            temp = array[low]
            array[low] = array[high - 1]
            array[high - 1] = pivot
            array[high] = temp
            high -= 1
        low += 1
    array[0:high] = quicksort(array[0:high])
    array[high:len(array)] = quicksort(array[high:len(array)])
    return array
    
test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))
import numpy as np
a = np.array([1, 2, 3, 4])
print(a[[False, True, False, False]])

table = np.array([[1, 3], [2, 4]])
print(table.max(axis=1))

z = {x: x*x for x in range(1, 100)}
print(z)