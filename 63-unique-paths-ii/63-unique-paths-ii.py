class Solution:
 
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        num_row, num_col = len(obstacleGrid), len(obstacleGrid[0])
        
        grid = [[1] * num_col for _ in range(num_row)]
        
        val = 1
        for row in range(num_row-1, -1, -1):
            if obstacleGrid[row][num_col-1] == 1:
                val = 0
            grid[row][num_col-1] = val
        
        val = 1
        for col in range(num_col-1, -1, -1):
            if obstacleGrid[num_row-1][col] == 1:
                val = 0
            grid[num_row-1][col] = val
        
        for row in range(num_row-2, -1, -1):
            for col in range(num_col-2, -1, -1):
                if obstacleGrid[row][col] == 1:
                    grid[row][col] = 0
                else:
                    grid[row][col] = grid[row+1][col] + grid[row][col+1]
        
        return grid[0][0]
            
        


#     def path_count(self, robot_row, robot_col, m, n, grid, memo):
#         # if target reached
#         if robot_row == m-1 and robot_col == n-1:
#             return 1
#         # if count to target present            
#         if (robot_row, robot_col) in memo:
#             return memo[robot_row, robot_col]
    
#         down = right = 0
#         #move down
#         if robot_row+1 <= m-1 and grid[robot_row+1][robot_col] == 0:
#             down = self.path_count(robot_row+1, robot_col, m, n, grid, memo)
#             memo[robot_row+1, robot_col] = down        
#         #move right
#         if robot_col+1 <= n-1 and grid[robot_row][robot_col+1] == 0:
#             right = self.path_count(robot_row, robot_col+1, m, n, grid, memo)
#             memo[robot_row, robot_col+1] = right
            
#         memo[robot_row, robot_col] = down + right
#         return memo[robot_row, robot_col]
        
#     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
#         if obstacleGrid[0][0] == 1:
#             return 0
        
#         m = len(obstacleGrid)
#         n = len(obstacleGrid[0])        
#         return self.path_count(0, 0, m, n, obstacleGrid, {})