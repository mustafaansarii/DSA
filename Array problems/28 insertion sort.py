def insertion_sort(arr,n):
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr


if __name__ == '__main__':
    arr=[2,34,45,5-4,445,34,0]
    print(insertion_sort(arr,len(arr)))