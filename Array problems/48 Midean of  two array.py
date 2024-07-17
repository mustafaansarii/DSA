def MideanofTwoArray(a,b,n,m):
    total_length = n + m
    mid_index = total_length // 2

    i = j = 0
    merged = []

    # Merge arrays until we reach the middle index
    while len(merged) <= mid_index:
        if i < n and (j >= m or a[i] <= b[j]):
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    return merged

if __name__ == '__main__':
    a=[1,2,3,4,5,6,7]
    b=[1,12,13,14,15,16,20,22,23,33]
    n=len(a)
    m=len(b)
    print(MideanofTwoArray(a,b,n,m))