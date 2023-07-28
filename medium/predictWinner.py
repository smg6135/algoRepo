class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        attempt 1: everytime player 1 picks, look at next two numbers that player 2 will pick
                   pick what minimizes the sum of next two numbers, two pointers

        attempt 2:  
        """
        memo = {}
        def maxscore(i,j):
            if (i,j) in memo:
                return memo[i,j]
            if i>j:
                return 0
            #
            sA = nums[i] + min( maxscore(i+1,j-1), maxscore(i+2,j  ) ) # pick A[i] + min of the 2 possible upcoming turns (player 2 is smart)
            sB = nums[j] + min( maxscore(i  ,j-2), maxscore(i+1,j-1) )
            score = max(sA,sB)
            memo[i,j] = score
            return score
        p1 = maxscore(0,len(nums)-1) # Score Player 1
        return p1>=(sum(nums)-p1) # p1 >= p2


solution = Solution().PredictTheWinner([3606449,6,5,9,452429,7,9580316,9857582,8514433,9,6,6614512,753594,5474165,4,2697293,8,7,1])
print(solution)



