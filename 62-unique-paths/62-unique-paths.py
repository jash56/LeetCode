class Solution:
    
    def rec(self, curr_row, curr_col, max_row, max_col, memo):
        if curr_row == max_row-1 and curr_col == max_col-1:
            return 1
        
        if (curr_row, curr_col) in memo:
            return memo[(curr_row, curr_col)]
            
        down = right = 0
        if curr_row+1 <= max_row-1:
            #move down
            down = self.rec(curr_row+1, curr_col, max_row, max_col, memo)
            memo[(curr_row+1, curr_col)] = down
            
        if curr_col+1 <= max_col-1:
            #move right
            right = self.rec(curr_row, curr_col+1, max_row, max_col, memo)
            memo[(curr_row, curr_col+1)] = right
        
        memo[(curr_row, curr_col)] = down + right
        return memo[(curr_row, curr_col)]
        
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}      
        return self.rec(curr_row=0, curr_col=0, max_row=m, max_col=n, memo=memo)