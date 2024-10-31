class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        n = len(self.stack) - 1
        if not self.min_stack:
            self.min_stack.append(0)
        else:
            if self.stack[n] <= self.stack[self.min_stack[-1]]:
                self.min_stack.append(n)

    def pop(self) -> None:
        if self.top() == self.getMin():
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.min_stack[-1]]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()