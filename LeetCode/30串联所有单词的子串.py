class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []
        re, wide, num, n = list(), len(words[0]), len(words), len(s)
        long = wide * num
        if n < long:
            return []
        words.sort()
        for i in range(n+1-long):
            l = [s[j:j+wide] for j in range(i, i+long, wide)]
            l.sort()
            if l == words:
                re.append(i)
        return re
