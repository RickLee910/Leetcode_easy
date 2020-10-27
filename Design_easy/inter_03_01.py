class TripleInOne:

    def __init__(self, stackSize: int):
        self.temp = [[] for i in range(3)]
        self.l = stackSize

    def push(self, stackNum: int, value: int) -> None:
        if len(self.temp[stackNum]) <=self.l:
            self.temp.append(value)

    def pop(self, stackNum: int) -> int:
        if len(self.temp[stackNum]) > 0:
            return self.temp[stackNum].pop(0)
        else:return -1
    def peek(self, stackNum: int) -> int:
        if len(self.temp[stackNum]) > 0:
            return self.temp[stackNum][-1]
        else:return -1

    def isEmpty(self, stackNum: int) -> bool:
        return len(self.temp[stackNum]) == 0

s = TripleInOne(18)
print(s.push(2,40))
print(s.pop(2))