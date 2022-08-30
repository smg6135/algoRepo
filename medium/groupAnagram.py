from ast import List
from collections import defaultdict
import string


class Solution:
    def groupAnagrams(self, strs):
        # time limit exceeded
        # sortedSplit = []
        # for i in range(len(strs)):
        #     sortedSplit.append(sorted([*strs[i]]))
        # res = []
        # added = []
        # for i in range(len(strs)):
        #     if i not in added:
        #         added.append(i)
        #         temp = [i]
        #         for j in range(i, len(strs)):
        #             if j not in added and sortedSplit[j] == sortedSplit[i]:
        #                 added.append(j)
        #                 temp.append(j)
        #         res.append(temp)
        # groupedRes = []
        # for strGroup in res:
        #     temp = []
        #     for index in strGroup:
        #         temp.append(strs[index])
        #     groupedRes.append(temp)
        # return groupedRes
        groups = defaultdict(list)
        
        for string in strs:
            groups[''.join(sorted(string))].append(string)
            
        return groups.values()

          
strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(strs))