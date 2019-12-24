通过next()在栈中缓存当前左子树的节点
from collections import deque
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.head = root
        self.stack = deque()
        
        while root:  #stack存左子节点
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """       

        cur = self.stack.pop()
        root = cur.right
        while root:  #stack存左子节点
            self.stack.append(root)
            root = root.left
        
        return cur.val


    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0

# 作者：user5707F
# 链接：https://leetcode-cn.com/problems/binary-search-tree-iterator/solution/nextshi-jian-fu-za-du-wei-o1-by-user5707f/

