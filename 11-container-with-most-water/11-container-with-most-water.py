class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = area = 0
        right = len(height)-1       
        while left < right:           
            area = max(area, (right-left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        return area
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        max_area = area = 0
        start, end = 0, len(height)-1
        while start != end:
            
            max_area = max(max_area, (end - start) * min(height[end], height[start]))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
                
            


        return max_area