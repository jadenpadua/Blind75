 import queue
from collections import defaultdict


# class of pqItem node
class pqItem:
    def __init__(self, count, word):
        self.count = count
        self.word = word
    
    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        ht = defaultdict(int)
        for word in words:
            ht[word] += 1
        
        pq = queue.PriorityQueue()
        for word in ht:
            item = pqItem(ht[word],word)
            if pq.qsize() < k:
                pq.put(item)
            else:
                # When comparison is returned true, it means the fir q element has hire prio, so don't
                # do anything and flip to false
                if not (item < pq.queue[0]):
                    pq.get()
                    pq.put(item)
        
        res = []
        while pq.qsize() > 0:
            res.append(pq.get().word)
        
        return res[::-1]
        
