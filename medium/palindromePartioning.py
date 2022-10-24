from itertools import chain, combinations

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        s = list(s)
        all_combination = chain.from_iterable(combinations(s, r) for r in range(len(s)+1))