


import collections
from typing import List


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
            d = collections.defaultdict(int)
            a = []
            b = []
            # Get all the points that img1 has as 1 and img2 has as 1
            for i in range(len(img1)):
                for j in range(len(img1[0])):
                    if(img1[i][j] == 1):
                        a.append((i,j))
                    if(img2[i][j] == 1):
                        b.append((i,j))
            ans = 0
            # for this part, take each coordinate and calculate the translation of the point
            # Using translation as the key, add 1 to each translation.
            # return the maximum value
            for t1 in a:
                for t2 in b:
                    t3 = (t2[0]-t1[0],t2[1]-t1[1])
                    d[t3] += 1
                    ans = max(ans, d[t3])
            return ans

img1 = [[1,1,0],[0,1,0],[0,1,0]]
img2 = [[0,0,0],[0,1,1],[0,0,1]]

Solution().largestOverlap(img1, img2)