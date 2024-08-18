def heapify(arr,n,i):
    while True:
        left=2*i+1
        right=2*i+2
        smallest=i

        if left < n and arr[left] > arr[smallest]:
            smallest=left

        if right < n and arr[right] > arr[smallest]:
            smallest=right

        if smallest==i:
            break
        arr[smallest],arr[i]=arr[i],arr[smallest]
        i=smallest
            

def HeapSort(arr,n):
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)

    for i in range(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        heapify(arr,i,0)


if __name__=="__main__":
    arr=[2,3,23,12,45,67,97,89,76]
    HeapSort(arr,len(arr))
    print(arr)