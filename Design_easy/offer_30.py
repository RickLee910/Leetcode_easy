class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []

    def push(self, x: int) -> None:
        self.l.append(x)

    def pop(self) -> None:
        self.l.pop()

    def top(self) -> int:
        return self.l[-1] if len(self.l) > 0 else -1

    def min(self) -> int:
        return min(self.l)if len(self.l) > 0 else -1