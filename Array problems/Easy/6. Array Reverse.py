# https://www.geeksforgeeks.org/program-to-reverse-an-array/

def Reverse(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            arr[j],arr[j+1]=arr[j+1],arr[j]

if __name__ == '__main__':
    arr=[[12,23,43,12,12,34,7,3,2,12],
         [12,4,5],
         []
         ]
    for ar in arr:
        Reverse(ar)
    print(arr)