class HashTable3:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def __setitem__(self, key, value):
        index = self.hash_function(key)
        original_index = index

        while self.table[index] is not None and (self.table[index][0] != key):
            index = (index + 1) % self.size
            if index == original_index:
                raise Exception("Hash table is full")
        
        self.table[index] = (key, value)

    def __getitem__(self, key):
        index = self.hash_function(key)
        original_index = index

        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == original_index:
                raise KeyError(f"Key {key} not found")
        
        raise KeyError(f"Key {key} not found")

    def __delitem__(self, key):
        index = self.hash_function(key)
        original_index = index

        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                # Rehash following elements to prevent breaking the probe sequence
                next_index = (index + 1) % self.size
                while self.table[next_index] is not None:
                    next_key, next_value = self.table[next_index]
                    self.table[next_index] = None
                    self.__setitem__(next_key, next_value)
                    next_index = (next_index + 1) % self.size
                return
            
            index = (index + 1) % self.size
            if index == original_index:
                raise KeyError(f"Key {key} not found")
        
        raise KeyError(f"Key {key} not found")

    def __str__(self):
        return str(self.table)

# Example usage
ht3 = HashTable3(5)

# Inserting values
ht3['key1'] = 'value1'
ht3['key11'] = 'value2'  # This will cause a collision and use linear probing
ht3['key21'] = 'value3'

print(ht3)  # Output: [None, (key11, 'value2'), None, None, (key21, 'value3')]

# Searching for values
print(ht3['key11'])  # Output: 'value2'

# Deleting a value
del ht3['key11']
print(ht3)  # Output: [None, None, None, None, (key21, 'value3')]
