# https://www.geeksforgeeks.org/union-and-intersection-of-two-sorted-arrays-2/

def intersection(a,b):
    j=0
    result = []
    for i in a:
        if i in b and i not in result:
            result.append(i)

    return result


if __name__ == '__main__':
    arr1 = [1, 2, 2, 2, 3]
    arr2 = [2, 3, 3, 4, 5, 5]
    print(intersection(arr1,arr2))

