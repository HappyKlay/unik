class MyCircularQueue:
    def __init__(self, k: int):
        self.size = k
        self.queue = [-1] * k
        self.front = -1
        self.rear = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return True

    def Front(self) -> int:
        return self.queue[self.front] if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.queue[self.rear] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.front == -1

    def isFull(self) -> bool:
        return (self.rear + 1) % self.size == self.front


commands = ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", 
            "Rear", "isFull", "deQueue", "enQueue", "Rear"]
values = [[3], [1], [2], [3], [4], [], [], [], [4], []]
output = []

myQueue = None
for cmd, val in zip(commands, values):
    if cmd == "MyCircularQueue":
        myQueue = MyCircularQueue(val[0])
        output.append(None)
    elif cmd == "enQueue":
        output.append(myQueue.enQueue(val[0]))
    elif cmd == "deQueue":
        output.append(myQueue.deQueue())
    elif cmd == "Front":
        output.append(myQueue.Front())
    elif cmd == "Rear":
        output.append(myQueue.Rear())
    elif cmd == "isEmpty":
        output.append(myQueue.isEmpty())
    elif cmd == "isFull":
        output.append(myQueue.isFull())

print(output)  # Output: [None, True, True, True, False, 3, True, True, True, 4]
