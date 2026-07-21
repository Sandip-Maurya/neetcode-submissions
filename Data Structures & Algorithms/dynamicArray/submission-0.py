class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.my_array = []


    def get(self, i: int) -> int:
        return self.my_array[i]


    def set(self, i: int, n: int) -> None:
        self.my_array[i] = n
        return


    def pushback(self, n: int) -> None:
        if self.getSize() == self.getCapacity():
            self.resize()
        self.my_array.append(n)        


    def popback(self) -> int:
        return self.my_array.pop()
 

    def resize(self) -> None:
        self.capacity = 2*self.capacity


    def getSize(self) -> int:
        return  len(self.my_array)
        
    
    def getCapacity(self) -> int:
        return self.capacity

