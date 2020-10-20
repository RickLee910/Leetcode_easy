class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.temp = []



    def push(self, x: int) -> None:
        self.temp.append(x)

    def pop(self) -> None:
        self.temp.pop()

    def top(self) -> int:
        return self.temp[-1]

    def getMin(self) -> int:
        return min(self.temp)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()