class Observer(ABC):
    @abstractmethod
    def notify(self, itemName: str) -> None:
        pass

class Customer(Observer):
    def __init__(self, name: str) -> None:
        self.name = name
        self.notifications = 0

    def notify(self, itemName: str) -> None:
        self.notifications += 1

    def countNotifications(self) -> int:
        return self.notifications

class OnlineStoreItem:
    def __init__(self, itemName: str, stock: int) -> None:
        self.itemName = itemName
        self.stock = stock
        self.subscribers : dict[Observer, int] = {}

    def subscribe(self, observer: Observer) -> None:
        self.subscribers[observer] = 0

    def unsubscribe(self, observer: Observer) -> None:
        self.subscribers.pop(observer)
        
    def updateStock(self, newStock: int) -> None:
        if not self.stock and newStock:
            for observer in self.subscribers:
                observer.notify(self.itemName)
        self.stock = newStock
        
