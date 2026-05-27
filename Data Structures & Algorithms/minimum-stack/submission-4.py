class MinStack:

    def __init__(self):
        self.myStack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.myStack.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        if not self.myStack:
            return
        
        if self.minStack and self.minStack[-1] == self.myStack.pop():
            self.minStack.pop()

    def top(self) -> int:
        if not self.myStack:
            return -1
        return self.myStack[-1]

    def getMin(self) -> int:
        if not self.minStack:
            return -1
        return self.minStack[-1]
        
