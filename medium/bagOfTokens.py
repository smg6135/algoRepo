from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        """
        classic greedy + 2 pointers
        sort the array and have two pointers least and most
        increment least if the power is less than tokens[least]
        if the power is less than the tokens[least], decrement most and add power with tokens[most]
        """
        sortedTokens = sorted(tokens)
        l_ptr = 0
        r_ptr = len(tokens) - 1
        max_score = 0
        score = 0
        while(l_ptr <= r_ptr):
            if sortedTokens[l_ptr] <= power:
                score += 1
                power -= sortedTokens[l_ptr]
                l_ptr += 1
            elif sortedTokens[l_ptr] > power and score >= 1:
                max_score = score
                score -= 1
                power += sortedTokens[r_ptr]
                r_ptr -= 1
            else:
                return max(max_score, score)
        return max(max_score, score)

tokens = [100,200]
Solution().bagOfTokensScore(tokens, 150)