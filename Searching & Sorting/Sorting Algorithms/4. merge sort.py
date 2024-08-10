def merge_sort2(arr, n):
    mid = n // 2
    if len(arr) > 1:
        left_arr2 = arr[:mid]
        right_arr2 = arr[mid:]

        merge_sort2(left_arr2, len(left_arr2))
        merge_sort2(right_arr2, len(right_arr2))

        i = 0
        j = 0
        k = 0
        while i < len(left_arr2) and j < len(right_arr2):
            if left_arr2[i] < right_arr2[j]:
                arr[k] = left_arr2[i]
                i += 1
            else:
                arr[k] = right_arr2[j]
                j += 1
            k += 1

        while i < len(left_arr2):
            arr[k] = left_arr2[i]
            i += 1
            k += 1

        while j < len(right_arr2):
            arr[k] = right_arr2[j]
            j += 1
            k += 1
if __name__ == '__main__':
    arr=[2,3,2,12]
    merge_sort2(arr,len(arr))
    print(arr)