def count_way(n):
    if n==2: return 2;
    if n==1: return  1;

    return count_way(n-1)+count_way(n-2)


if __name__ == '__main__':
    print(count_way(10))


 
