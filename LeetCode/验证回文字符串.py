class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        s = s.lower()
        left = 0
        right = len(s) - 1
        while left < right:
            if (s[left] in "1234567890qwertyuioplkjhgfdsazxcvbnm" and 
                s[right] in "1234567890qwertyuioplkjhgfdsazxcvbnm"):
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            else:
                if s[left] not in "1234567890qwertyuioplkjhgfdsazxcvbnm":
                    left += 1
                elif s[right] not in "1234567890qwertyuioplkjhgfdsazxcvbnm":
                    right -= 1 
        return True

        