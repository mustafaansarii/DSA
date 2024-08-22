#https://leetcode.com/problems/contains-duplicate/description/

from numpy import array
import numpy as np

arr = array([])
n = int(input("Enter size of Array: "))
while n > 0:
    num = int(input(f"Enter element: "))
    arr = np.append(arr, num)
    n -= 1
print(f"original array: {arr}")

def duplicates(arr):
    seen = set()
    for item in arr:
        if item in seen:
            return True
        seen.add(item)
    return False



print(duplicates(arr))

