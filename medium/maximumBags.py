class Solution(object):
    def maximumBags(self, capacity, rocks, additionalRocks):
        """
        :type capacity: List[int]
        :type rocks: List[int]
        :type additionalRocks: int
        :rtype: int
        """
        leftover = []
        for a, b in zip(capacity, rocks):
            leftover.append(a-b)

        if not leftover:
            return len(capacity)

        leftover = sorted(leftover, reverse=True)

        ct = 0
        while additionalRocks > 0 and leftover:
            curr = leftover.pop()
            if curr == 0:
                ct += 1
            else:
                additionalRocks -= curr
                ct += 1
        
        return ct

capacity = [2,3,4,5]
rocks = [1,2,4,4]
additionalRocks = 2

Solution().maximumBags(capacity, rocks, additionalRocks)