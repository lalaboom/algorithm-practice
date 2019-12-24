
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        from collections import defaultdict
        visited = set()
        res = set()
        for i in range(0, len(s) - 9):
            tmp = s[i:i+10]
            if tmp in visited:
                res.add(tmp)
            visited.add(tmp)
        return list(res)   

