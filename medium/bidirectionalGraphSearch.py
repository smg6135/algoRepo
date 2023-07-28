from collections import defaultdict, deque
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if not edges:
            return True

        bi_dict = defaultdict(list)
        for edge in edges:
            bi_dict[edge[0]].append(edge[1])
            bi_dict[edge[1]].append(edge[0])
        
        to_visit = deque()
        to_visit.append(source)
        seen = [source]

        while to_visit:
            curr_node = to_visit.popleft()
            
            if curr_node == destination:
                return True
            else:
                for next_node in bi_dict[curr_node]:
                    if next_node not in seen:
                        to_visit.append(next_node)
                        seen.append(next_node)

        return False

Solution().validPath(50, [[31,5],[10,46],[19,31],[5,1],[31,28],[28,29],[8,26],[13,23],[16,34],[30,1],[16,18],[33,46],[27,35],[2,25],[49,33],[44,19],[22,26],[30,13],[27,12],[8,16],[42,13],[18,3],[21,20],[2,17],[5,48],[41,37],[39,37],[2,11],[20,26],[19,43],[45,7],[0,21],[44,23],[2,39],[27,36],[41,48],[17,42],[40,32],[2,28],[35,38],[3,9],[41,30],[5,11],[24,22],[39,5],[40,31],[18,35],[23,39],[20,24],[45,12]]
, 29, 46)