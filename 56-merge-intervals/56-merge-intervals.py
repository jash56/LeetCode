class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x[0])
        ans = [intervals[0]]
        for interval in intervals[1:]:
            
            if ans[-1][1] >= interval[0]:
                ans[-1][1] = max(ans[-1][1], interval[1])
            else:
                ans.append(interval)
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if len(intervals) == 1: return intervals
#         intervals = sorted(intervals, key=lambda x: x[0])
        
#         final_intervals = [intervals[0]]

#         for interval in intervals:
            
#             if interval[0] <= final_intervals[-1][1]:
#                 final_intervals[-1][1] = max(interval[1], final_intervals[-1][-1])
#             else:
#                 final_intervals.append(interval)
                
#         return final_intervals