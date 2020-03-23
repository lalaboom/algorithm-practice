2行是中序遍历的代码，
分别是第8、16行；3行是更改节点指向的代码，
为13-15行。9-11行的if语句只有在中序遍历到第一个节点时调用，
自此之后listHead不变，listTail跟随算法的进度。
class Solution:
    def __init__(self):
        self.listHead = None
        self.listTail = None
    def Convert(self, pRootOfTree):
        if pRootOfTree==None:
            return
        self.Convert(pRootOfTree.left)
        if self.listHead==None:
            self.listHead = pRootOfTree
            self.listTail = pRootOfTree
        else:
            self.listTail.right = pRootOfTree
            pRootOfTree.left = self.listTail
            self.listTail = pRootOfTree
        self.Convert(pRootOfTree.right)
        return self.listHead
        







