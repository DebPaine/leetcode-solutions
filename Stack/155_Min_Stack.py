class MinStack:
    """
    Time: O(1) for all the methods
    Space: O(n), since we are using a stack
    """

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            min_val = val
        else:
            min_val = min(self.stack[-1][1], val)
        self.stack.append((val, min_val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
