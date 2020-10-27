class Solution:
    def subdomainVisits(self, cpdomains):
        d = {}
        for i in cpdomains:
            temp = i.split()
            temp1 = temp[1].split('.')
            for j in range(len(temp1)):
                flag = '.'.join(temp1[j:])
                if flag not in d.keys():
                    d[flag] = temp[0]
                else:
                    d[flag] = str(int(d[flag]) + int(temp[0]))
        ans = []
        for i in range(len(d)):
            ans.append(list(d.values())[i] + ' ' + list(d.keys())[i])
        return ans