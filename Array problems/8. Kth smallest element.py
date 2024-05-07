# https://www.geeksforgeeks.org/problems/kth-smallest-element5635/1
import sys
def kthSmallest(arr, l, r, k):
    if len(arr)==0:
        return
    min_index=sys.maxsize
    for i in range(len(arr)):
        if arr[i-1]<min_index:
            min_index=arr[k-1]
    return min_index


if __name__ == '__main__':
    array=[1,2,2
           3,4,5,6,72,8,9]
    print(kthSmallest(array,array[0],array[-1],3))

