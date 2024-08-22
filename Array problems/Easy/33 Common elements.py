#https://www.geeksforgeeks.org/problems/common-elements1132/1

class Solution:
    def commonElements(self,A, B, C, n1, n2, n3):
        A=set(A); B=set(B); C=set(C)
        a=[]
        for i in A:
            if i in B and i in C:
                a.append(i)
        return sorted(a)

if __name__ == '__main__':
    A=[1, 5, 10, 20, 40, 80]
    B=[6, 7, 20, 80, 100]
    C=[3, 4, 15, 20, 30, 70, 80, 120]
    print(Solution().commonElements(A, B, C, len(A), len(B), len(C)))