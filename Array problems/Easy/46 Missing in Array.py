def missingNumber(s, arr):
    # code here
    n = arr[s - 1]
    k = n*(n + 1) / 2
    l = sum(arr)
    return int(k-l)


arr=[1,3,4,5]
print(missingNumber(len(arr),arr))