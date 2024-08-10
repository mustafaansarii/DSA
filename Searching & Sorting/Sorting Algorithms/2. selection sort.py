def selection_sort(arr):
    size = len(arr)
    for i in range(size-1):
        min_index = i
        for j in range(min_index+1,size):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]

if __name__ == '__main__':
    arr=[32,4,1,4,22,5,4,23,12,1,5,78,5,54,3,22,12,21,15,6,5,3223,121]
    selection_sort(arr)
    print(arr)