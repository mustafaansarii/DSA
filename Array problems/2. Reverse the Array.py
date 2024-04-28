# https://www.geeksforgeeks.org/program-to-reverse-an-array/
from numpy import array
import numpy as np

arr = array([])
n = int(input("Enter size of Array: "))
while n > 0:
    num = int(input(f"Enter element: "))
    arr = np.append(arr, num)
    n -= 1
print(f"original array: {arr}")

def reverse_arr(arr):
    print("revesed array: ")
    for i in arr[::-1]:
        print(i, end=' ')

reverse_arr(arr)