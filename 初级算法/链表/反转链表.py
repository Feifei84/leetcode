'''
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
'''

from LinkList import *

# 迭代
def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    p = head
    q = None
    while p:
        t = p.next
        p.next = q
        q = p
        p = t
    return q

# 递归
def reverseList_V2(head: Optional[ListNode]) -> Optional[ListNode]:
    if head == None or head.next == None:
        return head
    p = reverseList_V2(head.next)
    head.next.next = head
    head.next = None
    return p


linklist = LinkList()
linklist.initList([1,2,3,4,5])
ans = reverseList_V2(linklist.head)
ans