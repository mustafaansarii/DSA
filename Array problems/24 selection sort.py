# https://www.geeksforgeeks.org/problems/selection-sort/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=selection-sort

class Solution:
    def select(self, arr, i, n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        return min_index

    def selectionSort(self, arr, n):
        for i in range(n - 1):
            min_index = self.select(arr, i, n)
            if min_index != i:
                arr[min_index], arr[i] = arr[i], arr[min_index]
        return arr
if __name__ == '__main__':
    arr=[4, 1, 3, 9, 7]
    Solution().selectionSort(arr,len(arr))
    print(arr)
