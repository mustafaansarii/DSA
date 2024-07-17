def isvalid(n):
    braces={"{":"}","[":"]","(":")"}
    stck=[]
    for i in n:
        if i in braces:
            stck.append(i)
    return stck






if __name__ == '__main__':
    n="{"
    print(isvalid(n))