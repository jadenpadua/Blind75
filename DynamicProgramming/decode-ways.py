# Use 262314 
class Solution:
    def numDecodings(self, s: str) -> int:
        
        def dfs(index, ht):
            
            if index == len(s):
                return 1
            
            if s[index] == "0":
                return 0
            
            
            if index in ht:
                return ht[index]
            
            
            if index + 2 <= len(s) and int(s[index: index + 2]) <= 26:
                single = dfs(index+1, ht)
                double = dfs(index+2, ht)
                ht[index] = single + double
                
            
            else:
                ht[index] = dfs(index+1, ht)
                
            return ht[index]
                
        
        ht = {}
        return dfs(0, ht)
