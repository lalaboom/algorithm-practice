class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # s = "my "
        # print(s.rstrip().split(" "))
        return(len(s.rstrip().split(" ")[-1]))