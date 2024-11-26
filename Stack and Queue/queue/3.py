from collections import deque

class RecentCounter:
    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()
        return len(self.requests)

commands = ["RecentCounter", "ping", "ping", "ping", "ping"]
values = [[], [1], [100], [3001], [3002]]
output = []

recentCounter = None
for cmd, val in zip(commands, values):
    if cmd == "RecentCounter":
        recentCounter = RecentCounter()
        output.append(None)
    elif cmd == "ping":
        output.append(recentCounter.ping(val[0]))

print(output)  # Output: [None, 1, 2, 3, 3]
