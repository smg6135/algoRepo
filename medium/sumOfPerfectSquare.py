class Solution:
    def numSquares(self, n: int) -> int:
        # dp approach
        # the minimum sum of i = minimum perfect sqaure sum of i - j + minimum perfect square sum of j

        # The dp array.
        dp = [float('inf')] * (n+1)
        
        for i in range(1,n+1):
            
            # calculate the square of i, dp[i_sq] to 1.
            i_sq = pow(i,2)
            if i_sq <= n:
                dp[i_sq] = 1
            
            # dp equation
            for j in range(i):
                dp[i] = min(dp[i],dp[i-j]+dp[j])

        return dp[n]

        # mathematical apporach
        # k = 1: Ruud's One-Square Theorem
        # k = 2: Fermat's Two-Square Theorem
        # k = 3: Legendre's Three-Square Theorem
        # k = 4: Lagrange's Four-Square Theorem

        i=1
        while i*i <= n:                             # case k = 1
            if i*i == n: return 1                   
            i+=1          

        def CheckTwo(c):                            # case k = 2 
            while c%2==0: c=c//2
            while c%5==0: c=c//5
            while c%9==0: c=c//9

            if c%3==0: return False

            if c in (0,1,13,17): return True

            i, j = 0, int(c**.5)

            while i <= j:
                if i*i + j*j == c: return True
                if i*i + j*j < c: i += 1
                if i*i + j*j > c: j -= 1

            return  False

        if CheckTwo(n): return 2

        while not n%4: n//=4                        # case k = 3  
        if n%8 != 7: return 3 
        
        return 4   