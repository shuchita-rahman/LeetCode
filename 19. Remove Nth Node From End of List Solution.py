# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int):
        a =[]
        temp = head
        
        while temp:
            a.append(temp)
            temp = temp.next     

        if len(a) == n:
            return head.next
        
        head =  a[len(a)-n-1]
        head.next = head.next.next
        head = a[0]
        return head
