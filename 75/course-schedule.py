class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        
        # create directed graph
        for pair in prerequisites:
            i, j = pair
            graph[i].append(j)
        
        for i in range(numCourses):
            # When dfs ends prematurely we found a cycle
            if not self.dfs(graph, visited, i):
                return False
        return True
    
    
    def dfs(self, graph, visited, i):
        # if ith node is visited, we found a cycle here
        if visited[i] == - 1:
            return False
        # if it is done processing, do not choose to revisit
        if visited[i] == 1:
            return True
        #mark as being visited
        visited[i] = -1
        
        # visit all neighbors
        for j in graph[i]:
            if not self.dfs(graph, visited, j):
                return False
        
        # after visiting all neighbors, mark as processed
        visited[i] = 1
        
        return True
            
