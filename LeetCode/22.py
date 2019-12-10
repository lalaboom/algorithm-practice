class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(left,right,tmp):
            if left==n and right==n:
                res.append(tmp)
                print(tmp)
                return
            if left<n:
                dfs(left+1,right,tmp+"(")
            if left>right and right<n:
                dfs(left,right+1,tmp+")")
        dfs(0,0,"")
        return res

# class Solution(object):
# 	def generateParenthesis(self, n):
# 		"""
# 		:type n: int
# 		:rtype: List[str]
# 		"""
# 		res = []
# 		# 递归函数
# 		def dfs(left,right,tmp):
# 			# 递归函数的终止条件
# 			if left==n and right==n:
# 				res.append(tmp)
# 				return
# 			# 注意左括号的数量要小于参数n，即输入的n为3时
# 			# 最多只能生成3个左括号
# 			if left<n:
# 				dfs(left+1,right,tmp+"(")
# 			# 右括号的数量也要小于n，左括号的数量要 大于 右括号数量
# 			# 因为 ((( 是合法的(假设程序还没处理完)
# 			# 而),)),)))都是不合法的
# 			if left>right and right<n:
# 				dfs(left,right+1,tmp+")")
# 		dfs(0,0,"")
# 		return res

# 作者：user7439t
# 链接：https://leetcode-cn.com/problems/generate-parentheses/solution/dong-hua-yan-shi-22-gua-hao-sheng-cheng-by-user743/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。