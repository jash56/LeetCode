class Solution:
    
    def path_count(self, robot_row, robot_col, m, n, grid, memo):
        
        if robot_row == m-1 and robot_col == n-1:
            if grid[robot_row][robot_col] == 0:       
                return 1
            else:
                return 0
        
        if (robot_row, robot_col) in memo:
            return memo[robot_row, robot_col]
        
        down = right = 0
        
        if robot_row+1 <= m-1 and grid[robot_row+1][robot_col] == 0:
            down = self.path_count(robot_row+1, robot_col, m, n, grid, memo)
            memo[robot_row+1, robot_col] = down
            
        if robot_col+1 <= n-1 and grid[robot_row][robot_col+1] == 0:
            right = self.path_count(robot_row, robot_col+1, m, n, grid, memo)
            memo[robot_row, robot_col+1] = right
            
        memo[robot_row, robot_col] = down + right
        return memo[robot_row, robot_col]
        
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        memo = {}
        
        return self.path_count(0, 0, m, n, obstacleGrid, memo)