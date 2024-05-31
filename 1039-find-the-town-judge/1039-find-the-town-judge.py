class Solution(object):
    def findJudge(self, n, trust):
        outgoing = {i: 0 for i in range(1, n + 1)}
        incoming = {i: 0 for i in range(1, n + 1)}

        for i in range(len(trust)):
            outgoing[trust[i][0]] += 1
            incoming[trust[i][1]] += 1

        for key in incoming.keys():
            if incoming[key] == n - 1 and outgoing[key] == 0:
                return key
        return -1
        