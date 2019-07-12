# 序列化二叉树

# # 题目：

# 请实现两个函数，分别用来序列化和反序列化二叉树

# # 思路：

# 使用前序遍历来序列化和发序列化即可。
class Solution:
    def Serialize(self, root):
        if root == None:
            return "#"
        return str(root.val) + "," + self.Serialize(root.left) + "," + self.Serialize(root.right)
        # write code here
    def Deserialize(self, s):
        #root, index = self.de(s.split(","), 0)
        root = self.de(s.split(","))
        return root
    def de(self,list):
        if len(list) <= 0:
            return None
        val = list.pop(0)
        root = None
        if val != '#':
            root = TreeNode(int(val))
            root.left = self.de(list)
            root.right = self.de(list)
        return root