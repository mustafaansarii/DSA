class Solution:
    def findRelativeRanks(self, score):
        if len(score)==1:
                score[0] = "Gold Medal"
                return score
        
        f=sorted(score)
        if len(score)>=1:
            if f[-1] in score:
                index_to_replace = score.index(f[-1])
                score[index_to_replace] = "Gold Medal"
        if len(score)>=2:
            if f[-2] in score:
                index_to_replace = score.index(f[-2])
                score[index_to_replace] = "Silver Medal"

        if len(score)>=3:
            if f[-3] in score:
                index_to_replace = score.index(f[-3])
                score[index_to_replace] = "Bronze Medal"

        if len(score)>3:
            s=(f[0:-3])
            s=s[::-1]
            for i in range(len(s)):
                index_to_replace = score.index(s[i])
                score[index_to_replace] = str(4+i)
        else:
            return score
        
        return score

if __name__ == "__main__":
    arr = [10,2]
    print(Solution().findRelativeRanks(arr))
