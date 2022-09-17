from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        backward, res = {}, []
        # backwords word
        for i, word in enumerate(words):
            backward[word[::-1]] = i

        for i, word in enumerate(words):
            
            # if the word is in the backward word and it's not in the same index
            # add
            if word in backward and backward[word] != i:
                res.append([i, backward[word]])
                
            # if the word is empty that's just palindrome
            if word != "" and "" in backward and word == word[::-1]:
                res.append([i, backward[""]])
                res.append([backward[""], i])
            
            # if there is a word that is partially 'palindrome'
            # such as "sssll", "lls"
            # check the 
            for j in range(len(word)):
                if word[j:] in backward and word[:j] == word[j-1::-1]:
                    res.append([backward[word[j:]], i])
                if word[:j] in backward and word[j:] == word[:j-1:-1]:
                    res.append([i, backward[word[:j]]])
                    
        return res

Solution().palindromePairs(["abcd","dcba","lls","s","sssll"])