"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node: return
        
        ht = {node: Node(node.val)}
        queue = deque([node])
        
        while queue:
            currNode = queue.popleft()
            for neighbor in currNode.neighbors:
                if neighbor not in ht:
                    ht[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                
                ht[currNode].neighbors.append(ht[neighbor])
                
        return ht[node]
