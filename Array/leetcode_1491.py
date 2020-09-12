class Solution:
    def average(self, salary):
        salary.sort()
        res = (sum(salary) - salary[0] - salary[-1]) / (len(salary) - 2)
        return res
