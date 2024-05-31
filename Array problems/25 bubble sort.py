def bubble_sort(arr,n):
    for i in range(n):
        swapped=True
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break

if __name__ == '__main__':
    arr=[32,4,2,1-1,3,23,4,0,23,-23]
    bubble_sort(arr,len(arr))
    print(arr)