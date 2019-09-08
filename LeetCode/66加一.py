class Solution(object):
    def plusOne(self, digits):
        sums = 0
        for i in range(len(digits)):
            sums += 10**(len(digits)-1-i)*digits[i]
        sums_str = str(sums + 1)
        return [int(j) for j in sums_str]