# https://www.geeksforgeeks.org/move-negative-numbers-beginning-positive-end-constant-extra-space/

def Move_all_negative(arr: object, n):
    j=0
    for i in range(n):
        if (arr[i] < 0):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j = j + 1

if __name__ == '__main__':
    arr = [10, 2, 4, -5, 2, -7, 3, 2, -6, -8, -9, 3, 2, -1]
    Move_all_negative(arr,len(arr))
    print(arr)