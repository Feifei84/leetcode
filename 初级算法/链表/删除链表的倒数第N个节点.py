'''
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
'''
from LinkList import *

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    def get_len(head: Optional[ListNode]) -> int:
        i = 0
        while head:
            i += 1
            head = head.next
        return i

    len = get_len(head)
    front = ListNode(0, head)

    p = front
    for i in range(0, len - n):
        p = p.next
    p.next = p.next.next
    return front.next

# 双指针法
def removeNthFromEnd_V2(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    front = ListNode(0, head)
    p = front
    q = front
    for i in range(n):
        p = p.next
    while p.next:
        p = p.next
        q = q.next
    q.next = q.next.next
    return front.next

linklist = LinkList()
linklist.initList([1])
l = removeNthFromEnd_V2(linklist.head, 1)
l