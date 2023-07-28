class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text2)
        m = len(text1)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if text2[i] == text1[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])

        return dp[0][0]

text1 = "bsbininm"
text2 = "jmjkbkjkv"

print(Solution().longestCommonSubsequence(text1, text2))