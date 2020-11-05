
def crush(s):

    if not s:
        return s

    stack = []
    stack.append([s[0], 1])
    for i in range(1,len(s)):
        print(stack)
        if s[i] != s[i-1]:
            if stack[-1][1] >= 3:
                stack.pop()

            if stack and stack[-1][0] == s[i]:
                stack[-1][1] += 1
            
            else:
                stack.append([s[i], 1])
            
        else:
            stack[-1][1] += 1
    

    if stack[-1][1] >= 3:
        stack.pop()
    
    res = []
    for entry in stack:
        res += entry[0] * entry[1]
    
    return ''.join(res)



print(crush("aaabbbc"))
print(crush("aaabbbacd"))
print(crush("aabbccddeeedcba"))
