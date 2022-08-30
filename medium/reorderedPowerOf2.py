
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        """
        brute force
        """
        i = 0
        nSorted = sorted(n)
        while i < 30:
            comp = sorted(2 ** i)
            if(nSorted == comp):
                return True
        return False