
from collections import deque
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:

        def validNeighbour(curr, candidate):
            return sum([1 for i in 8 if curr[i] != candidate[i]]) == 1

        # initial queue

        ct = 0
        temp_queue = deque([start])
        visited = set()
        while temp_queue:

            for _ in len(temp_queue):
                next_queue = temp_queue.popleft()

                if next_queue == end:
                    return ct
                
                for content in bank:
                    if validNeighbour(content, next_queue) and content not in visited:
                        next_queue.append(content)
                        visited.add(content)
            ct += 1

        return -1

start = "AACCGGTT"
end = "AAACGGTA"
bank = ["AACCGATT","AACCGATA","AAACGATA","AAACGGTA"]
Solution().minMutation(start, end, bank)
