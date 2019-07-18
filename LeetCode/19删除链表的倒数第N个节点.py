


	# 取整除 - 返回商的整数部分


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:return 
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        while n:
            fast = fast.next
            n -= 1
        slow = dummy
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next










