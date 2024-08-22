def Binary_search(arr,left,right,target):
    if left>right:
        return -1
    mid=(left+right)//2
    if arr[mid]==target:
        return mid
    if arr[mid]>target:
        return Binary_search(arr,left,mid-1,target)
    if arr[mid]<target:
        return Binary_search(arr,mid+1,right,target)

if __name__ == '__main__':
    arr=[1,2,3,4,67,78]
    print(Binary_search(arr,0,len(arr)-1,2))