# 二叉树的下一个结点

# # 题目：

# 给定一个二叉树和其中的一个结点，
# 请找出中序遍历顺序的下一个结点并且返回。注意，
# 树中的结点不仅包含左右子结点，同时包含指向父结点的指针。

# # 思路：

# 如果一个结点有右子树，
# 那么它的下一个结点就是它的右子树的最左子结点。
# 也就是说从右子结点出发一直沿着指向左子树结点的指针，
# 我们就能找到它的下一个结点。
# 例如，图中结点b的下一个结点是h，
# 结点a的下一个结点是f。

# 接着我们分析一下结点没有右子树的情形。
# 如果结点是它父结点的左子结点，
# 那么它的下一个结点就是它的父结点。
# 例如，途中结点d的下一个结点是b，f的下一个结点是c。

# 如果一个结点既没有右子树，
# 并且它还是父结点的右子结点，这种情形就比较复杂。
# 我们可以沿着指向父结点的指针一直向上遍历，
# 直到找到一个是它父结点的左子结点的结点。
# 如果这样的结点存在，
# 那么这个结点的父结点就是我们要找的下一个结点

class Solution:
    def GetNext(self, pNode):
        if not pNode:
            return None #null？
        if pNode.right:
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            return pNode
        while pNode.next:
            if pNode.next.left == pNode:
                return pNode.next
            pNode = pNode.next
        return None

