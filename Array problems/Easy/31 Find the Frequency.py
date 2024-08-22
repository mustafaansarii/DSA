# https://www.geeksforgeeks.org/problems/find-the-frequency/1

def frequency(arr,x):
    a=[]
    for i in arr:
        if i==x:
            a.append(i)
    return len(a)


if __name__ == '__main__':
    arr=[1, 2, 3, 3, 2, 1]
    print(frequency(arr,1))