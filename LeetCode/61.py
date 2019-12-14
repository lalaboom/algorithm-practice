class Solution(object):
	def rotateRight(self, head, k):
		"""
		:type head: ListNode
		:type k: int
		:rtype: ListNode
		"""
		# 下面有 if n==0 ...判断了，所以开头的判断可以省略
		#if not head or k<=0:
		#    return head
		# 创建一个特殊节点，快指针，慢指针，统计节点个数的cur
		p = ListNode(-1)
		cur,n,low,fast,p.next = head,0,p,p,head
		# 统计链表个数
		while cur:
			cur,n = cur.next,n+1
		# 边界条件不用忘记处理了	
		if n==0 or k%n==0:
			return head
		# 还有一个边界条件不要忘了，k可能大于n，所以要取模
		n = k%n
		# 快指针先移动n步
		while fast.next and n>0:
			fast,n = fast.next,n-1
		# 快指针，慢指针一起移动，找到需要切割的点
		while fast.next:
			low,fast = low.next,fast.next
		# 改变链表的指向关系，注意这里的步骤不要乱了
		# 先让fast节点指向head(也就是p.next)
		# 再是head(也就是p.next)指向low的下一个节点
		# 这两步如果弄反了就会出现节点丢失了
		# 最后不要忘记将low.next置空
		fast.next,p.next,low.next = head,low.next,None
		return p.next

# 作者：user7439t
# 链接：https://leetcode-cn.com/problems/rotate-list/solution/dong-hua-yan-shi-61-xuan-zhuan-lian-biao-by-user74/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
