class Solution:
    def get_neighbors(self, curr, grid):
        #up left down right
        offset = ((-1,0), (0,-1), (1, 0), (0, 1))
        row_size = len(grid)
        col_size = len(grid[0])
        ans = []
        for direction in offset:
            temp = (direction[0]+curr[0], direction[1]+curr[1])
            if 0 <= temp[0] < row_size and 0 <= temp[1] < col_size and grid[temp[0]][temp[1]] == '1':
                ans.append(temp)
        return ans
        
    def explore_island(self, curr, grid):       
        if not curr: return  
        grid[curr[0]][curr[1]] = '0'
        for neighbor in self.get_neighbors(curr, grid):
            self.explore_island(neighbor, grid)
        
    def numIslands(self, grid: List[List[str]]) -> int:         
        if not grid: return 0
        island = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])): 
                if grid[row][col] == '1':
                    island += 1  
                    self.explore_island((row, col), grid)
        return island
                