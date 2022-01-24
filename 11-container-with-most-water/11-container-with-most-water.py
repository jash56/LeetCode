class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = area = 0
        start, end = 0, len(height)-1
        while start != end:
            
            max_area = max(max_area, (end - start) * min(height[end], height[start]))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
                
            


        return max_area