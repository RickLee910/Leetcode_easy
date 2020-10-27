class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key = []
        self.value = []

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        if key in self.key:
            self.value[self.key.index(key)] = value
        else:
            self.key.append(key)
            self.value.append(value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key in self.key:
            return self.value[self.key.index(key)]
        else:
            return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """

        self.value.pop(self.key.index(key))
        self.key.remove(key)
