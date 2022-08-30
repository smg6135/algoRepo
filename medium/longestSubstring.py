from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # queue approach 
        longest = 0
        repeat = deque()
        index = 0
        while index < len(s):
            if s[index] not in repeat:
                repeat.append(s[index])
                index+= 1
            else:
                if longest < len(repeat):
                    longest = len(repeat)
                repeat.popleft()
        return max(len(repeat), longest)
        


print(Solution().lengthOfLongestSubstring("abcabcbb"))