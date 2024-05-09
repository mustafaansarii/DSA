#https://www.geeksforgeeks.org/print-all-the-duplicates-in-the-input-string/

def duplicate(char):
    for i in char:
        count = char.count(i)
        if count > 1:
            print(f"{i}, count= {count}")

if __name__ == '__main__':
    char = "geeksforgeeks"
    duplicate(char)
