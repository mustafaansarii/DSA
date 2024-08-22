# find power of an element

def find_power(a, n):
    if n == 0:
        return 1
    elif n == 1:
        return a
    elif n < 0:
        return 1 / find_power(a, -n)
    else:
        mid = n // 2
        b = find_power(a, mid)
        result = b * b
        if n % 2 != 0:
            result *= a
        return result



if __name__ == '__main__':
    print(find_power(50,-2))
