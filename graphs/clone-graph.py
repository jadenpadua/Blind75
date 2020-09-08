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
         # map original nodes to their clones
        d = {node : Node(node.val)}
        q = deque([node])
        while q:
                    currNode = q.popleft()
                    for nei in currNode.neighbors:
                        if nei not in d:
                         # store copy of the neighboring node
                            d[nei] = Node(nei.val)
                            q.append(nei)
                     # connect the node copy at hand to its neighboring nodes (also copies) -------- [1]
                        d[currNode].neighbors.append(d[nei])
                        
        return d[node]
