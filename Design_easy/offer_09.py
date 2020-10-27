class CQueue:

    def __init__(self):
        self.temp = []

    def appendTail(self, value: int) -> None:
        self.temp.append(value)

    def deleteHead(self) -> int:
        if self.temp != []:return self.temp.pop()
        else: return -1