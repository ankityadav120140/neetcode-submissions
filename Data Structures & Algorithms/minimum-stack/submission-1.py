class MinStack:

    q = collections.deque()
    minDeq = collections.deque()

    def __init__(self):
        pass

    def push(self, val: int) -> None:
        self.q.append(val)
        

    def pop(self) -> None:
        self.q.pop()

    def top(self) -> int:
        return self.q[-1]

    def getMin(self) -> int:
        return min(self.q)
