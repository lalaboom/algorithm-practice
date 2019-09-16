class Solution(object):
    def firstBadVersion(self, n):
        left ,right = 1,n
        while left <right:
            middle = (left+right)//2
            if isBadVersion(middle):
                right = middle
            else:
                left = middle+1
        return left
        """
        :type n: int
        :rtype: int
        """