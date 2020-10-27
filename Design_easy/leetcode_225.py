
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.d.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.d.pop() if len(self.d) > 0 else -1

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.d[-1] if len(self.d) > 0 else -1

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.d) == 0