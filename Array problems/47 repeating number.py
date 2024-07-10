from typing import List
def duplicates(n: int, arr: List[int]) -> List[int]:
    extra_list=[]
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]==arr[j]:
                extra_list.append(arr[i])
    if len(extra_list)>0:
        return extra_list
    return -1



array=[1,2,3]
print(duplicates(len(array),array))