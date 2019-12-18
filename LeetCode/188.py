class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        de = collections.deque()
        de.append((root, 1))
        while de:
            p, dep = de.popleft()
            if not p.left and not p.right:
                return dep
            if p.left:
                de.append((p.left, dep+1))
            if p.right:
                de.append((p.right, dep+1))