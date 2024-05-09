# https://www.geeksforgeeks.org/problems/union-of-two-arrays3538/1
class Solution:
    # Function to return the count of number of elements in union of two arrays.
    def doUnion(self ,a ,n ,b ,m):
        for i in range(m):
            if b[i] not in a:
                a.append(b[i])
        return (len(a))

        # s1=set(b)
        # s2=set(a)
        # print(s1.union(s2))
        # print(len(s1.union(s2)))



if __name__ == '__main__':
    array1=[85, 25, 1 ,32, 54 ,6]
    array2=[85, 2 ]
    Solution().doUnion(array1,len(array1),array2,len(array2))
