

#enumerate() 函数用于将一个可遍历的数据对象


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    # 直接对两个链表操作；对应节点上的值做加法运算，过10则进位。位数不够则补0
    def addTwoNumbers(self, l1, l2):
        l = ListNode(0)
        l_copy = l
        #进位符
        carry = 0
        while l1 or l2: #两个表头都为空时才停止
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            two_sum = l1_val + l2_val + carry
            if two_sum < 10:
                l_copy.next = ListNode(two_sum)
                carry = 0
            else:
                carry = two_sum//10
                l_copy.next = ListNode(two_sum%10)
            l_copy = l_copy.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry > 0:
            l_copy.next = ListNode(carry)
        return l.next



