from tkinter.tix import InputOnly


def bubble_sort(input_array):
    length = len(input_array)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if input_array[j] > input_array[j + 1]:
                input_array[j], input_array[j+1] = input_array[j+1], input_array[j]

#test
test_array = [3, 5, 1, 29, 34, 32, 22, 11]

bubble_sort(test_array)
print(test_array)