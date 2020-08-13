class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        ht = {}
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in ht:
                ht[sorted_word] = [word]
            
            else:
                ht[sorted_word].append(word)
        
        for key in ht:
            anagrams.append(ht[key])
        
        return anagrams
