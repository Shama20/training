def Sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1    
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key

d = input("enter size numbers").split()
data=[int (x) for x in d]
Sort(data)
print('Sorted Array in Ascending Order:')
print(data)