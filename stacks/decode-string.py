class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        currString = ""
        count = 0
        
        for char in s:
            if char == "[":
                stack.append((currString, count))
                currString = ""
                count = 0
            
            elif char == "]":
                lastString, lastCount = stack.pop(-1)
                currString = lastString + lastCount * currString
            
            elif char.isdigit():
                count = count * 10 + int(char)
            
            else:
                currString += char
                
            print(stack, count, currString)
        
        return currString
