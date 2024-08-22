class Solution:
    def kthSmallest(self,arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function'''
        for i in range(len(arr)):
            swapped=True
            for j in range(len(arr)-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
                    swapp=True
            if not swapped:
                break
        return arr[k-1]

if __name__ == '__main__':
    arr=[7 ,10, 4, 20 ,15]
    k=4
    print(Solution().kthSmallest(arr,0,len(arr)-1,k))