
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        temp = head
        if (not temp) or (not temp.next):
            return temp
        
        temp.next, current, previous = None, temp.next, temp
        
        while(current.next):
            current.next, current, previous = previous, current.next, current 
        current.next = previous
        return current
        
        
