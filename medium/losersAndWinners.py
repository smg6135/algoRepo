from collections import defaultdict
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = defaultdict(int)
        losers = defaultdict(int)

        # wins everything
        # exact one loses

        for match in matches:
            won = match[0]
            loss = match[1]
            losers[loss] += 1
            winners[won] += 1
        
        losers_ans = []
        for k, v in losers.items():
            if winners[k]:
                winners.pop(k)
            else:
                winners.pop(k)
            if v == 1:
                losers_ans.append(k)
        return [sorted(list(winners.keys())), sorted(losers_ans)]

matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
print(Solution().findWinners(matches))