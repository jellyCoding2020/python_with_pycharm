def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print (selectionSort([5, 0, 3, 14, 6, 10, 1, 4, -2, 9, 7, 12, 8, 15, 13, 2, 11, -1]))
#print (selectionSort([6*2, 2*3]))