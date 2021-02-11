#abaxyzzyxf
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestPalindrome = [0,1]
        
        for i in range(1, len(s)):
            odd = self.getLongestPalindromeFrom(s, i-1, i+1)
            even = self.getLongestPalindromeFrom(s, i-1, i)
            
            currLongest = max(odd, even, key = lambda x: x[1] - x[0])
            longestPalindrome = max(longestPalindrome, currLongest, key = lambda x: x[1] - x[0])
        
        return s[longestPalindrome[0] : longestPalindrome[1]]
            
        
    def getLongestPalindromeFrom(self, s, left, right):
        
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                break
            left -= 1
            right += 1
            
        return [left + 1, right]
            
