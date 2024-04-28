# https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/
from numpy import array
import numpy as np

arr = array([])
n = int(input("Enter size of Array: "))
while n > 0:
    num = int(input(f"Enter element: "))
    arr = np.append(arr, num)
    n -= 1
print(f"original array: {arr}")

def min_max(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    print(f"max: {arr[-1]}, min: {arr[0]}")



min_max(arr)
print(f"sorted array: {arr}")
