class MinStack:

    def __init__(self):
        self.q = collections.deque()
        self.minDeq = collections.deque()

    def push(self, val: int) -> None:
        self.q.append(val)
        if not self.minDeq:
            self.minDeq.append(val)
        else:
            self.minDeq.append(min(val, self.minDeq[-1]))

    def pop(self) -> None:
        self.q.pop()
        self.minDeq.pop()

    def top(self) -> int:
        return self.q[-1]

    def getMin(self) -> int:
        return self.minDeq[-1] if self.minDeq else None
