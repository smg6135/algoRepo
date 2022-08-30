class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        idea: if the substring s[i:j] is palindrome, s[i-1:j+1] will be also true
             if s[i-1] and s[j+1] is same
        """
        # result: start and end of the palindrome
        start, end = 0, 0
        # DP approach
        dp_results = [[False] * len(s) for i in range(len(s))]

        # every 1 letter string is true
        for i in range(len(s)):
            for j in range(len(s)):
                if i == j:
                    dp_results[i][j] = True

        # every 2 letter is palindrome if two letters are equal
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                dp_results[i][i+1] = True
                # if start == end:
                if not start and not end: # this is faster
                    start = i
                    end = i+1
        
        # for the rest, dp_results[i][j] is true when
        # 1. dp_results[i+1][j-1] is true
        # 2. and string[i] == string[j]
        # ex) for substring(2, 5) to be true,
        #       1. substring(3, 4) has to be true
        #       2. and string[2] and string[5] has to be same as noted above
        for k in range(2, len(s)):
            for i in range(len(s)-2):
                # i is the start of the substring
                # j is the end of the substring
                # have to fill it (0, 2), (1, 3)... so on since the dp uses previous result to find out
                # whether the next one is true or not
                j = i + k
                if j >= len(s):
                    break
                if dp_results[i+1][j-1] == True and s[i] == s[j]:
                    dp_results[i][j] = True
                    if j - i > end - start:
                        end = j
                        start = i

        return s[start:end+1]


print(Solution().longestPalindrome("aaaaa"))