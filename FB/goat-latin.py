class Solution:
    def toGoatLatin(self, S: str) -> str:
        split = S.split(' ')
        vowels = "aeiou"
        goatLatin = []
        
        aCount = 1
        
        for word in split:
            goatWord = ""
            if word[0].lower() in vowels:
                goatWord = word + "ma"
            elif word[0].isalpha():
                goatWord = word[1:] + word[0] + "ma"
            
            goatWord = goatWord + "a"*aCount
            goatLatin.append(goatWord)
            aCount += 1
            
        return ' '.join(goatLatin)
        
