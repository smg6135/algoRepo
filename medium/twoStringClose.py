from collections import defaultdict


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        s_word1 = sorted(word1)
        s_word2 = sorted(word2)
        if len(word1) != len(word2):
            return False
        
        if s_word1 == s_word2:
            return True
        
        c_word1 = defaultdict(int)
        c_word2 = defaultdict(int)
        for i, char in enumerate(s_word1):
            c_word1[char] += 1
            c_word2[s_word2[i]] += 1
        
        for vals in zip(sorted(c_word1.values()), sorted(c_word2.values())):
            if vals[0] != vals[1]:
                return False
        
        for keys in zip(sorted(c_word1.keys(), c_word2.keys())):
            if keys[0] != keys[1]:
                return False

        return True
    
Solution().closeStrings('cabbba', "abbccc")