class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return []
        queue = [root]
        out = []
        while queue:
            child = []                      
            node = []                      
            for item in queue:              
                child.append(item.val)       
                if item.left:
                    node.append(item.left)  
                if item.right:
                    node.append(item.right)
            out.append(child)                
            queue = node                     
        return out
