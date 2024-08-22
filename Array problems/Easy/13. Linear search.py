#
def linear_search(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    return "not found"
if __name__ == '__main__':
    arr=[1,2,3,4,5,6,7,9,11,-1,6]
    print(linear_search(arr,-1))