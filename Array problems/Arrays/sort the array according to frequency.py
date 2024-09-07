
from collections import Counter
class Solution:
    def sortByFreq(self,arr):
        frequency = Counter(arr)
        sorted_arr = sorted(arr, key=lambda x: (-frequency[x], x))
        
        return sorted_arr
a=Solution().sortByFreq([12,23,34,2,12,12,23])
print(a)