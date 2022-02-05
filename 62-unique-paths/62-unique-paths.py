class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1]*n for _ in range(m)]
        
        for row in range(m-2, -1, -1):
            for col in range(n-2, -1, -1):
                # print(row, col)
                grid[row][col] = grid[row+1][col] + grid[row][col+1]
                
        return grid[0][0]
    
    
    
# recursive with memoization
#     def rec(self, curr_row, curr_col, max_row, max_col, memo):
#         if curr_row == max_row-1 and curr_col == max_col-1:
#             return 1
        
#         if (curr_row, curr_col) in memo:
#             return memo[(curr_row, curr_col)]
            
#         down = right = 0
#         if curr_row+1 <= max_row-1:
#             #move down
#             down = self.rec(curr_row+1, curr_col, max_row, max_col, memo)
#             memo[(curr_row+1, curr_col)] = down
            
#         if curr_col+1 <= max_col-1:
#             #move right
#             right = self.rec(curr_row, curr_col+1, max_row, max_col, memo)
#             memo[(curr_row, curr_col+1)] = right
        
#         memo[(curr_row, curr_col)] = down + right
#         return memo[(curr_row, curr_col)]

    
#     def uniquePaths(self, m: int, n: int) -> int:
#         memo = {}      
#         return self.rec(curr_row=0, curr_col=0, max_row=m, max_col=n, memo=memo)