from collections import deque
class AnimalShelf:

    def __init__(self):
        self.d = deque()

    def enqueue(self, animal) -> None:
        self.d.append(animal[0])

    def dequeueAny(self):
        return self.d.popleft() if len(self.d) > 0 else [-1,-1]

    def dequeueDog(self):
        for i in range(len(self.d)):
            if self.d[i][1] ==1:
                return self.d.pop(i)
        return [-1,-1]

    def dequeueCat(self):
        for i in range(len(self.d)):
            if self.d[i][1] ==0:
                return self.d.popleft()
        return [-1,-1]
s = AnimalShelf()
s.enqueue([[0,0]])
s.enqueue([[1,0]])
print(s.dequeueCat())
print(s.dequeueDog())
print(s.dequeueAny())