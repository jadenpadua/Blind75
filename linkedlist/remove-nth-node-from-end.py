class Solution:
    def removeNthFromEnd(self, head, n):
        first = head
        second = head
        
        for i in range(n):
            second = second.next
            
        if not second:
            return head.next
        
        while second.next:
            second = second.next
            first = first.next
            
        first.next = first.next.next
        
        return head
