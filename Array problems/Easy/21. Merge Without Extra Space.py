# https://www.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1
class Solution:

    # Function to merge the arrays.
    def merge(self, arr1, arr2, n, m):
        # a=[]
        # for i in arr1:
        #     a.append(i)
        #
        # for i in arr2:
        #     a.append(i)
        # b=sorted(a)
        #
        # arr1=[]
        # for i in range(n):
        #     arr1.append(b[i])
        # return (arr1)
        # arr2=[]
        # for i in range(n,len(b)):
        #     arr2.append(b[i])
        # return (arr2)
        #
    # def merge(self,arr1,arr2,n,m):
        arr1.extend(arr2)
        arr2.clear()
        return sorted(arr1)





if __name__ == '__main__':
    n = 4
    arr1= [1 ,3 ,5, 7]
    m = 5
    arr2= [0 ,2, 6, 8 ,9]
    print(Solution().merge(arr1, arr2, n, m))

    # Output:
    # arr1[] = [0 1 2 3]
    # arr2[] = [5 6 7 8 9]