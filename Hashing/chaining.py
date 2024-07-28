class hash_table2:
    def __init__(self, size) -> None:
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        value = 0
        for i in key:
            value += ord(i)
        return value % self.size
    
    def __setitem__(self, key, value):
        index = self.hash_function(key)
        for i in range(len(self.table[index])):
            if key == self.table[index][i][0]:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def __getitem__(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if key == k:
                return v
        raise KeyError(f"Key '{key}' not found!")

    def __delitem__(self, key):
        index = self.hash_function(key)
        for i in range(len(self.table[index])):
            if self.table[index][i][0] == key:
                del self.table[index][i]
                return
        raise KeyError(f"Key '{key}' not found!")

    def __contains__(self, key):
        index = self.hash_function(key)
        return any(k == key for k, _ in self.table[index])

# Example usage
ht2 = hash_table2(5)
ht2['apple'] = 10
ht2['banana'] = 20
print(ht2['banana']) 
ht2['banana'] = 30

print(ht2['apple'])   # Output: 10
print(ht2['banana'])  # Output: 20

# Check if a key exists
print('apple' in ht2)  # Output: True
print('orange' in ht2) # Output: False

# Delete a key
del ht2['apple']
print('apple' in ht2)  # Output: False
