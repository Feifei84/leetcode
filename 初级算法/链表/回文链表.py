'''
给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。
'''

from LinkList import *
# 方法1：遍历单链表中元素并存到列表中，然后判断列表与其转置是否相等
class Solution1:
    def isPalindrome(self, head: ListNode) -> bool:
        val_list = []
        while head:
            val_list.append(head.val)
            head = head.next
        return val_list == val_list[::-1]
# 时间复杂度：O(n),空间复杂度：O(n)

# 方法2：递归
# 注：通过递归实现反向遍历链表
def print_val_in_reverse(head:ListNode):
    if head:
        print_val_in_reverse(head.next)
        print(head.val)
# 思路：使用递归反向向前遍历节点，同时使用递归函数外的变量向后遍历
class Solution2:
    def isPalindrome(self, head: ListNode) -> bool:
        self.left = head
        def palindrome_check(head:ListNode):
            # if head:  # 官方题解用这个if判断，则left要从左遍历到最右，递归中的head要从右遍历到最左，直到为none，但实际left只需遍历一半即可
            if head and (head != self.left or head.next != self.left):  #用这个if判断，当有奇数个节点时head != self.left继续执行递归，否则直接返回True因为左右均已遍历了一半元素，当有偶数个节点时head.next != self.left则继续执行递归进行判断，否则直接返回True
                # 第一个if：当深层递归判断出的最i前的元素与第i后的元素已不满足对称相等时，则必不回文，下一层递归中直接返回false，不再执行该层递归的后续代码
                if not palindrome_check(head.next):
                    return False
                # 第二个if：满足第一个if，但若当前递归层的head.val != left.val，也直接返回false，不再执行该层递归的后续代码，返回到前一层递归
                if head.val != self.left.val:
                    return False
                # 前面节点与对称位置的后面节点的比较中，前面节点向后要手动实现，后面节点向前通过递归实现
                self.left = self.left.next
            return True
        return palindrome_check(head)
# 时间复杂度：O(n)，空间复杂度：O(n)。

# 方法3：
# 如何避免使用O(n)额外空间？方法就是原地改变，即改变输入的head自身。
# 可以将链表的后半部分反转（修改链表结构），然后将前半部分和后半部分进行比较。

class Solution3:

    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        # 找到前半部分链表的尾节点并反转后半部分链表
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # 判断是否回文
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # 还原链表并返回结果
        first_half_end.next = self.reverse_list(second_half_start)
        return result

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous
# 时间复杂度：O(n)，空间复杂度：O(1)。
