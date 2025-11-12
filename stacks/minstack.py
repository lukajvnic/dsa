from collections import deque


class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = deque([])

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minstack) > 0 and val <= self.minstack[0]:
            self.minstack.appendleft(val)
        else:
            self.minstack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if len(self.minstack) > 0 and val == self.minstack[0]:
            self.minstack.popleft()
        else:
            self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[0]

    def __str__(self):
        return f"---\nStack: {self.stack}\nMinstack: {self.minstack}"
        
s = MinStack()
s.push(-2)
print(s)
s.push(-3)
print(s)
s.pop()
print(s)


