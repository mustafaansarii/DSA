def selection_sort(arr,n):
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr

if __name__ == '__main__':
    arr=[2,4,6,-22,7,64,34,23,4,-12,0,65,2]
    print(selection_sort(arr,len(arr)))


