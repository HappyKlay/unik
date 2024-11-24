class MyCircularDeque:
    def __init__(self, k: int):
        self.size = k
        self.queue = [-1] * k
        self.front = 0
        self.rear = -1
        self.count = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1 + self.size) % self.size
        self.queue[self.front] = value
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.queue[self.front] = -1
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.queue[self.rear] = -1
        self.rear = (self.rear - 1 + self.size) % self.size
        self.count -= 1
        return True

    def getFront(self) -> int:
        return self.queue[self.front] if not self.isEmpty() else -1

    def getRear(self) -> int:
        return self.queue[self.rear] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size


commands = ["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront",
            "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
values = [[3], [1], [2], [3], [4], [], [], [], [4], []]
output = []

myDeque = None
for cmd, val in zip(commands, values):
    if cmd == "MyCircularDeque":
        myDeque = MyCircularDeque(val[0])
        output.append(None)
    elif cmd == "insertLast":
        output.append(myDeque.insertLast(val[0]))
    elif cmd == "insertFront":
        output.append(myDeque.insertFront(val[0]))
    elif cmd == "deleteLast":
        output.append(myDeque.deleteLast())
    elif cmd == "deleteFront":
        output.append(myDeque.deleteFront())
    elif cmd == "getFront":
        output.append(myDeque.getFront())
    elif cmd == "getRear":
        output.append(myDeque.getRear())
    elif cmd == "isEmpty":
        output.append(myDeque.isEmpty())
    elif cmd == "isFull":
        output.append(myDeque.isFull())

print(output)  # Output: [None, True, True, True, False, 2, True, True, True, 4]
