# https://www.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1
def sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]


if __name__ == '__main__':
    arr=[23,45,23]
    sort(arr)
    print(arr)
    arr=[]
    a=[[2,45,43,33,],
       [23,4,6],
       [],[1,2,3,4,3,6]]

    for i in a:
        sort(i)
        print(i)
