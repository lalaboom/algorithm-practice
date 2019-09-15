class Solution(object):
    def sortedArrayToBST(self, nums):
        if len(nums)==0:
            return
        # 取nums列表的中间下标值
        # print(TreeNode(nums[1]))
        mid_index = len(nums)//2
        pNode = TreeNode(nums[mid_index])
        pNode.left = self.sortedArrayToBST(nums[:mid_index])
        pNode.right = self.sortedArrayToBST(nums[mid_index+1:])
        return pNode

        """
        :type nums: List[int]
        :rtype: TreeNode
        """
