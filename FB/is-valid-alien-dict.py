class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ht = dict()
        index = 0
        for i in range(len(order)):
            ht[order[i]] = ht.get(order[i],1) + i 
        
        print(ht)
        
        for i in range(1, len(words)):
            if self.compare(words[i-1], words[i], ht) > 0:
                return False
        return True
    
    def compare(self, word1, word2, ht):
        i = 0
        j = 0
        char_compare_value = 0
        while i < len(word1) and j < len(word2) and char_compare_value == 0:
            
            char_compare_value = ht[word1[i]] - ht[word2[j]]
            i += 1
            j += 1

        if char_compare_value == 0:
            return len(word1) - len(word2)
        else:
            return char_compare_value
