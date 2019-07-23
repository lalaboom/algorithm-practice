


	# 取整除 - 返回商的整数部分



class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre = ListNode(0)
        res = pre
        while head and head.next:
            nex  = head.next.next
            pre.next = head.next
            pre = head
            head.next.next = head
            head = nex
        pre.next = head
        return res.next











