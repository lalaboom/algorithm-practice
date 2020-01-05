class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        # 找到翻转链表部分的前一个节点, 1->2->3->4->5->NULL, m = 2, n = 4 指的是 节点值为1
        for _ in range(m-1):
            pre = pre.next
        # print(pre.val)
        # 用双指针,进行链表翻转
        node = None
        cur = pre.next
        for _ in range(n-m+1):
            tmp = cur.next
            cur.next = node
            node = cur
            cur = tmp
        # 将翻转部分 和 原链表拼接
        pre.next.next = cur
        pre.next = node
        return dummy.next