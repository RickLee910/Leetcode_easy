class Solution:
    def busyStudent(self, startTime, endTime, queryTime: int) -> int:
        count = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime and  endTime[i] >= queryTime:
                count += 1
        return count