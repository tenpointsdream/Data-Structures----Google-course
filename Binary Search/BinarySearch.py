def binary_search(input_array, value):
    lower = 0
    higher = len(input_array) - 1
    while lower <= higher:
        middle = (lower + higher) // 2
        if input_array[middle] == value:
            return middle
        if input_array[middle] < value:
            lower = middle + 1
        else:
            higher = middle - 1 
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15

print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))