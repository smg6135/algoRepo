class Solution:
    def minWindow(self, s: str, t: str) -> str:
        track = t
        for char in s:
            if char == track[0]:
                # TODO:::