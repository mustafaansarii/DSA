# https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article
class Solution:
    def missingNumber(self,array,n):
        sum_n=n+1
        total_sum = sum_n*(sum_n+1)/2
        array_sum =0
        for i in array:
            array_sum +=i

        return int(total_sum-array_sum)


if __name__ == '__main__':
    arr=[1,2,3,5]
    print(Solution().missingNumber(arr,len(arr)))