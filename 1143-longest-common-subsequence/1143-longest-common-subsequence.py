class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # does not work for some reason         
        # dp = [[None]*(len(text2)+1)] * (len(text1)+1) 
        dp = [[None]*(len(text2)+1) for _ in range(len(text1)+1)]        
        for row in range(len(text1)+1):
            for col in range(len(text2)+1): 
                if row == 0 or col == 0:
                    dp[row][col] = 0
                elif text1[row-1] == text2[col-1]:
                    dp[row][col] = dp[row-1][col-1] + 1
                else:
                    dp[row][col] = max(dp[row-1][col], dp[row][col-1])
        
        return dp[len(text1)][len(text2)]
        
                
                    
            