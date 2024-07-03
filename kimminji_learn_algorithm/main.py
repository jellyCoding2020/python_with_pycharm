#------------plus-----------
'''
def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

print(sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
'''

#------------------quicksort---------------------
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
print (quicksort([10-2, 7*2*2, 5+7, 2, 3*3, 6/2, 14, 19, 12+3, 4]))