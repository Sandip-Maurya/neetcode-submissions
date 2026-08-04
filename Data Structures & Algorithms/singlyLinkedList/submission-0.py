class LinkedList:
    
    def __init__(self):
        self.linked_list: list[int] = []

    
    def get(self, index: int) -> int:
        if index <  len(self.linked_list):
            return self.linked_list[index]
        return -1
        

    def insertHead(self, val: int) -> None:
        self.linked_list = [val] + self.linked_list
        

    def insertTail(self, val: int) -> None:
        self.linked_list.append(val)
        
        

    def remove(self, index: int) -> bool:
        if index <  len(self.linked_list):
            self.linked_list.pop(index)
            return True
        return False
        

    def getValues(self) -> List[int]:
        return self.linked_list
        
