# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue

#TC: O(NLOG(K))
#SC: O(N) where n is total nodes of list

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        k = len(lists)
        pQueue = PriorityQueue(maxsize=k)
        
        dummy = ListNode(-1)
        curr = dummy
        
        #put nodes in pq ordered by first LL nodes in the List
        for list_idx, node in enumerate(lists):
            if node is not None:
                pQueue.put((node.val, list_idx, node))
        
        while pQueue.qsize() > 0:
            popped = pQueue.get()
            curr.next, list_idx = popped[2], popped[1]
            curr = curr.next
            
            #now reorders priority to the curr.next.val and rearranges queue in that way
            if curr.next:
                pQueue.put((curr.next.val, list_idx, curr.next))
        
        return dummy.next
        return dummy.next
