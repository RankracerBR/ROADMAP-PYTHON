class HashTable:
    def __init__(self,capacity):
        self.capacity = capacity * [None]
    
    def __len__(self):
        return len(self.values)