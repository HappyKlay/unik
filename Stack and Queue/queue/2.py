from collections import deque

class MyStack:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        self.queue2.append(x)
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        return self.queue1.popleft()

    def top(self) -> int:
        return self.queue1[0]

    def empty(self) -> bool:
        return not self.queue1

commands = ["MyStack", "push", "push", "top", "pop", "empty"]
values = [[], [1], [2], [], [], []]
output = []

myStack = None
for cmd, val in zip(commands, values):
    if cmd == "MyStack":
        myStack = MyStack()
        output.append(None)
    elif cmd == "push":
        myStack.push(val[0])
        output.append(None)
    elif cmd == "pop":
        output.append(myStack.pop())
    elif cmd == "top":
        output.append(myStack.top())
    elif cmd == "empty":
        output.append(myStack.empty())

print(output)  # Output: [None, None, None, 2, 2, False]
