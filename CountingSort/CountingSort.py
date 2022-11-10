def CountingSort(array):
    size = len(array)
    max = 0
    for i in range(0, size):
        if array[i] > max:
            max = array[i]
    
    count = [0] * (max + 1)
    for i in range(0, size):
        count[array[i]] += 1
    #print(count)
    for i in range(1, len(count)):
        count[i] += count[i-1]
    #print(count)
    outArray = [0] * size
    i = size - 1
    while i >= 0:
        outArray[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1
    print(outArray)
test = [7,7,3,6,3,10,1,5,7]
CountingSort(test)
#print(test)