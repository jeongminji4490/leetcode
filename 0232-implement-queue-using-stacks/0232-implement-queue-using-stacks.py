class MyQueue:

    def __init__(self):
        self.stack = []
        self.reversed = []
        self.size = 0

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.size += 1

    def pop(self) -> int:
        if self.empty():
            return -1
        else:
            if not self.reversed:
                for i in range(self.size):
                    self.reversed.append(self.stack.pop())
            self.size -= 1
        return self.reversed.pop()

    def peek(self) -> int:
        if self.empty():
            return -1
        else:
            if not self.reversed:
                for i in range(self.size):
                    self.reversed.append(self.stack.pop())
            return self.reversed[-1]

    def empty(self) -> bool:
        return True if not self.stack and not self.reversed else False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()