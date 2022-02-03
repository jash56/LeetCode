class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        modify_row, modify_col = set(), set()
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    modify_row.add(row)
                    modify_col.add(col)
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row in modify_row or col in modify_col:
                    matrix[row][col] = 0 
                
        
            
                