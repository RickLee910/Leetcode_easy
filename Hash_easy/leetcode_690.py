"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
import collections
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        temp = {}
        for i in employees:
            temp[i.id] = [i.importance, i.subordinates]
        q = collections.deque([id])
        ans = 0
        while q:
            temp1 = q.popleft()
            for i in range(len(temp[temp1][1])):
                q.append(temp[temp1][1][i])
            ans += temp[temp1][0]
        return ans