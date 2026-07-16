class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_table = {}


    def insert(self, key: int, value: int) -> None:
        self.hash_table[key] = value
        if len(self.hash_table) >= self.capacity/2:
            self.resize()
        print(self.capacity)


    def get(self, key: int) -> int:
        return self.hash_table.get(key, -1)


    def remove(self, key: int) -> bool:
        if key not in self.hash_table:
            return False
        
        self.hash_table.pop(key)
        return True

    def getSize(self) -> int:
        return len(self.hash_table)


    def getCapacity(self) -> int:
        return self.capacity


    def resize(self) -> None:
        self.capacity = 2*self.capacity


