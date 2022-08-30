from cgitb import reset


class Solution:
    def helpCount(self, s: str) -> str:
        # helper that converts say -> count
        # if say "11" -> count 2 1s -> "21"
        res = ""
        currChar = s[0]
        ct = 0
        for c in s:
            if currChar != c:
                res += str(ct) + currChar
                currChar = c
                ct = 1
            else:
                ct += 1
        return res + str(ct) + currChar

    def countAndSay(self, n: int) -> str:
        # base case
        if n == 1:
            return "1"
        
        # we want to count the previous say
        else:
            return self.helpCount(self.countAndSay(n-1))

print(Solution().countAndSay(4))