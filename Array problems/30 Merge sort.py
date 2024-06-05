def merge(arr,left,right,mid):
    left_arr=
def merge_sort(arr,left,right):
    mid=left+(right-left)//2
    if left==right:
        return arr
    merge_sort(arr,left,mid-1)
    merge_sort(arr,mid+1,right)
    merge(arr,left,right,mid)
    return arr






if __name__ == '__main__':
    arr=[23,5,2]
    print(merge_sort(arr,0,len(arr)))