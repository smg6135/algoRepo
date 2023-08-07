from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        
        memo = {}

        # setting up the mid point and build left and right based on the mid point
        # for n = 5, we can set mid point such that we use 1 node on left, 3 on right
        # or 2 on left and 2 on right or 3 on left and 1 on right
        # if we can make all possible lefts and all possible rights
        # attach to main root node, we get all possible results

        def _recursiveFBT(n):
            # if we already know how to build w certain n
            # memoization return
            if n in memo:
                return memo[n]

            ret = []
            if n == 1:
                # if 1 there's only 1 possibility
                ret.append(TreeNode(0))
            else:
                for i in range(1, n-1, 2):
                    # all possible lefts
                    left_t = _recursiveFBT(i)
                    # all possible rights 
                    right_t = _recursiveFBT(n-i-1)

                    for lt in left_t:
                        for rt in right_t:
                            ret.append(TreeNode(0, lt, rt))
            memo[n] = ret
            return ret
        
        return _recursiveFBT(n)


    

Solution().allPossibleFBT(5)