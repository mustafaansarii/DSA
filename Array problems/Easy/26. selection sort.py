def select(arr,n,i):
    min_index=i
    for i in range(i+1,n):
        if arr[i]<arr[min_index]:
            min_index=i
    return min_index
def sort(arr,n):
    for j in range(n-1):
        min_index=select(arr,n,j)
        if min_index!=j:
            arr[min_index],arr[j]=arr[j],arr[min_index]
    return arr


if __name__ == '__main__':
    arr=[23,5,6,3,-3,23,45,7,-13,0,2,0]
    print(sort(arr,len(arr)))

