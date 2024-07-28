class QuadraticProbingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.count = 0

    def hash_function(self, key):
        return hash(key) % self.size

    def __setitem__(self, key, value):
        index = self.hash_function(key)
        c1, c2 = 1, 0  # Coefficients for quadratic probing

        for i in range(self.size):
            probing_index = (index + c1 * i**2 + c2 * i) % self.size
            if self.table[probing_index] is None or self.table[probing_index][0] == key:
                self.table[probing_index] = (key, value)
                self.count += 1
                return
        
        raise Exception("Hash table is full")

    def __getitem__(self, key):
        index = self.hash_function(key)
        c1, c2 = 1, 0  # Coefficients for quadratic probing

        for i in range(self.size):
            probing_index = (index + c1 * i**2 + c2 * i) % self.size
            if self.table[probing_index] is None:
                raise KeyError(f"Key {key} not found")
            if self.table[probing_index][0] == key:
                return self.table[probing_index][1]
        
        raise KeyError(f"Key {key} not found")

    def __delitem__(self, key):
        index = self.hash_function(key)
        c1, c2 = 1, 0  # Coefficients for quadratic probing

        for i in range(self.size):
            probing_index = (index + c1 * i**2 + c2 * i) % self.size
            if self.table[probing_index] is None:
                raise KeyError(f"Key {key} not found")
            if self.table[probing_index][0] == key:
                self.table[probing_index] = None
                self.count -= 1
                return
        
        raise KeyError(f"Key {key} not found")

    def __str__(self):
        return str(self.table)

# Example usage
ht = QuadraticProbingHashTable(size=7)

# Inserting values
ht['key1'] = 'value1'
ht['key8'] = 'value2'  # This will cause a collision and use quadratic probing
ht['key15'] = 'value3'

print(ht)  # Output might vary depending on probing sequence

# Searching for values
print(ht['key8'])  # Output: 'value2'

# Deleting a value
del ht['key8']
print(ht)  # Output: Table without the deleted key
