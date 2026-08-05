class Deque:
    
    def __init__(self):
        self._deque = []


    def isEmpty(self) -> bool:
        return not bool(self._deque)
        

    def append(self, value: int) -> None:
        self._deque.append(value)
        

    def appendleft(self, value: int) -> None:
        self._deque.insert(0, value)
        

    def pop(self) -> int:
        return self._deque.pop() if self._deque else -1
        

    def popleft(self) -> int:
        return self._deque.pop(0) if self._deque else -1

        
