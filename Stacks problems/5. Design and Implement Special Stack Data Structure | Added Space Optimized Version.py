# Design and Implement Special Stack Data Structure | Added Space Optimized Version
# https://www.geeksforgeeks.org/problems/special-stack/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article

# Your task is to complete all these function's
# function should append an element on to the stack
def push(arr, ele):
    # Code here
    arr.append(ele)


# Function should pop an element from stack
def pop(arr):
    # Code here
    if len(arr) != 0:
        arr.pop()


# function should return 1/0 or True/False
def isFull(n, arr):
    # Code here
    if len(arr) != n:
        return False
    else:
        return True


# function should return 1/0 or True/False
def isEmpty(arr):
    # Code here
    if len(arr) == 0:
        return True
    else:
        return False


# function should return minimum element from the stack
def getMin(n, arr):
    # Code here
    if len(arr) > 0:
        return min(arr)
    else:
        return


# {
# Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        stack = []
        while (not isEmpty(stack)):
            pop(stack)

        for i in range(n):
            push(stack, arr[i])
        print(getMin(n, stack))
# contributed by: Harshit Sidhwa

# } Driver Code Ends