from array import array
class Bubble_sort:
    def sort(self,arr):
        for i in range(len(arr)):
            for j in range(len(arr)-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]

if __name__ == '__main__':
    B=Bubble_sort()
    arr=array("i",[23,54,2,3,5,21,65,1,7,98,1,5,8,1])
    print("unsorted array: ")
    for i in arr:
        print(i, end=' ')
    B.sort(arr)
    print("\nsorted array: ")
    for i in arr:
        print(i, end=' ')
    arr=["z","x","m","e","r"]
    print("\nunsorted array: ")
    for i in arr:
        print(i,end=' ')
    B.sort(arr)
    print("\nsorted array: ")
    for i in arr:
        print(i,end=' ')