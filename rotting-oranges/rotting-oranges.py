from collections import deque
class Solution:
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #implementing BFS
        
        bfs_queue = deque()
        fresh_count = 0
        time_elapsed = -1
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    bfs_queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh_count += 1
        bfs_queue.append((-1, -1))  
        
        while bfs_queue:
            cell = bfs_queue.popleft()
            if cell == (-1, -1):
                time_elapsed += 1
                if bfs_queue:
                    bfs_queue.append((-1, -1))  
            else:   
                for i, j in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    if 0 <= (cell[0] + i) < len(grid) and 0 <= (cell[1] + j) < len(grid[0]):
                        print(i, j)
                        if grid[cell[0] + i][cell[1] + j] == 1:
                            print(i ,j)
                            bfs_queue.append((cell[0] + i, cell[1] + j))
                            fresh_count -= 1
                            grid[cell[0] + i][cell[1] + j] = 2

        if fresh_count == 0:
            return time_elapsed
        else:
            return -1
        
                    
            
                
        
        
        
        