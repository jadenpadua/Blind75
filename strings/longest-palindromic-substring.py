class Solution:
    def longestPalindrome(self, s: str) -> str:
        #abaxyzzyxf
        currentLongest = [0,1]
    
        for i in range(1,len(s)):
            odd = self.getLongestPalindromeFrom(s,i-1,i+1)
            even = self.getLongestPalindromeFrom(s,i-1,i)
            
            longest = max(odd, even, key = lambda x: x[1] - x[0])
            currentLongest = max(longest,currentLongest,key = lambda x: x[1] - x[0])
                 
        return s[currentLongest[0]:currentLongest[1]]
            
    def getLongestPalindromeFrom(self,string,left,right):
        while left >= 0 and right < len(string):
            if string[left] != string[right]:
                break
            left -= 1
            right += 1
        return [left + 1, right]
            
