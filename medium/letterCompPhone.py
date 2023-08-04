from typing import List


g_digits = ["", "","abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # backtracking
        # 80% faster

        if len(digits) == 1:
            return [*g_digits[int(digits)]]

        res = []

        iter_digit = digits[1:]
        temp_digits = [*g_digits[int(digits[0])]]

        poss_comps = self.letterCombinations(iter_digit)

        temp_comp = []

        for comp in poss_comps:
            for dig in temp_digits:
                temp_comp.append(comp+dig)

        res += temp_comp
        
        return res

print(Solution().letterCombinations("23"))