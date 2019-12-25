# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 先找到链表的中点：快慢指针，考虑节点个数奇偶情况
# 再翻转后半段链表
# 最后两链表依次插入
class Solution:
    def reorderList(self, head: ListNode) -> None:

        # 查找中点
        fast = slow = a = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next    
        b = slow.next if fast else slow
        
        # 翻转中点之后链表 #用pre存储?
        pre = None
        cur = b
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
            
        # 交叉合并
        b = pre
        while a:
            a.next, b = b, a.next
            a = a.next
        return head