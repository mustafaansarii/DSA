#https://www.geeksforgeeks.org/problems/count-digits5716/1

class Solution:
    def evenlyDivides (self, N):
        a=(str(N))
        if "0" in a:
            a = a.replace("0", "")
        b=0
        for i in range(len(a)):
            if N%int(a[i])==0:
                b+=1
        return b


if __name__ == '__main__':
    print(Solution().evenlyDivides(26435))