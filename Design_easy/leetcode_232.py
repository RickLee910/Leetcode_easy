from collections import deque
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = deque()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.d.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.d.popleft()


    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.d[0] if len(self.d) > 0 else -1

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.d) == 0