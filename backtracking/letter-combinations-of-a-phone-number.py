class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if digits is None or len(digits) == 0:
            return res
        
        mapping = {
        '1': '',
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
        '0': ' '
        }
        
        def backtrack(i, curr):
            if i == len(digits):
                if len(curr) > 0:
                    res.append(''.join(curr))
                return
            
            for letter in mapping[digits[i]]:
                curr.append(letter)
                backtrack(i+1, curr)
                curr.pop()
    
        backtrack(0, [])
        
        return res
