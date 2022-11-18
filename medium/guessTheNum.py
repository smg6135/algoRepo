class Solution:
    # this is not medium but just added since it's generic binary search form and I like it
    def guess(self, n, pick):
        if n < pick:
            return -1
        if n > pick:
            return 1
        return 0
    def guessNumber(self, n: int, pick) -> int:
        l, h = 1, n
        mid = (l + h) // 2
        guess_num = self.guess(mid, pick)
        while guess_num != 0:
            if guess_num == -1:
                l = mid
            else:
                h = mid
            mid = (l + h) // 2
            guess_num = self.guess(mid, pick)
        return mid
Solution().guessNumber(10, 6)