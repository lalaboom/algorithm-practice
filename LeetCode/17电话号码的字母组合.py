


	# 取整除 - 返回商的整数部分



class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
            m = {
                '2': list('abc'),
                '3': list('def'),
                '4': list('ghi'),
                '5': list('jkl'),
                '6': list('mno'),
                '7': list('pqrs'),
                '8': list('tuv'),
                '9': list('wxyz'),
                }
            if not digits:
                return []
            res = ['']
            for i in digits:
                res = [x + y for x in res for y in m[i]]
            return res


                









