# https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/
from array import array
import sys
def min(arr):
    if len(arr)==0:
        return
    min_index=sys.maxsize
    for i in range(len(arr)):
        if arr[i]<min_index:
            min_index=arr[i]
    return min_index
def max(arr):
    if len(arr)==0:
        return
    min_index=float("-inf")
    for i in range(len(arr)):
        if arr[i]>min_index:
            min_index=arr[i]
    return min_index

if __name__ == '__main__':
    # Valid input
    arr1 = array("i", [2, 4, 5, 12, 1, 3, 4])
    print("Minimum:", min(arr1))
    print("Maximum:", max(arr1))

    # Empty array
    arr2 = array("i", [])
    print("Minimum:", min(arr2))
    print("Maximum:", max(arr2))

    arr3 = array("i", [-2, -4, -5, -12, -1, -3, -4])
    print("Minimum:", min(arr3))
    print("Maximum:", max(arr3))

    arr4 = array("i", [2, 4, 5, 12, 1, 3, 4, 4, 5])
    print("Minimum:", min(arr4))
    print("Maximum:", max(arr4))

    arr5 = array("i", [7])
    print("Minimum:", min(arr5))
    print("Maximum:", max(arr5))

    # Large array
    arr6 = array("i", range(1000000))
    print("Minimum:", min(arr6))
    print("Maximum:", max(arr6))





