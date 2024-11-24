class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2

myQueue = MyQueue()
myQueue.push(1)        # queue is: [1]
myQueue.push(2)        # queue is: [1, 2]
print(myQueue.peek())  # Output: 1
print(myQueue.pop())   # Output: 1, queue is now [2]
print(myQueue.empty()) # Output: False
