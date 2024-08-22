#https://www.geeksforgeeks.org/problems/reverse-array-in-groups0255/1
class Solution:
    # Function to reverse every sub-array group of size k.
    def reverseInGroups(self, arr, N, K):
        # Iterate over the array in chunks of size K
        for i in range(0, N, K):
            # Find the right boundary of the current chunk
            left = i
            right = min(i + K - 1, N - 1)
            # Reverse the current chunk
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        return arr

if __name__ == '__main__':
    arr=[1,2,3,4,5]
    k=4
    print(Solution().reverseInGroups(arr,len(arr),3))
