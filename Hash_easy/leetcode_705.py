class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.temp = set()


    def add(self, key: int) -> None:
        self.temp.add(key)

    def remove(self, key: int) -> None:
        if key in self.temp:self.temp.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.temp

s = MyHashSet()
s.add(9)
print(s)