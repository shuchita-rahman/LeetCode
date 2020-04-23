class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        head = l1
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1 and l2 is None:
            return l1
        else:
            while head.next is not None:
                head = head.next
            head.next = l2
            head = l1

            while head is not None:
                temp = head.next
                while temp is not None:
                    if head.val > temp.val:
                        t = head.val
                        head.val = temp.val
                        temp.val = t
                    temp = temp.next
                head = head.next
            return l1

    
