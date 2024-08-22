from typing import List
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize==0:
            return True
        return False

if __name__ == '__main__':
    array=[1,2,3,4,5]
    print(Solution().isNStraightHand(array,4))
